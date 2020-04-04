### --------------------------------------------------- ###
### ----- Session 6+7: Linear ML for econometrics ----- ###
### -------------------- IV Model --------------------- ###

### The approach in this exercise follows the ideas of the paper Chernozhukov et al. - see Onenote.
### The paper and the exercises are based on the following equations:
### y_𝑖 = 𝛼_0 d_𝑖 + x′_𝑖 𝛽_0 + 𝜈_𝑖     (main)
### d_𝑖 = x′_𝑖 𝛾_0 + z′_𝑖 𝛿_0 + u_𝑖    (aux)
### BE AWARE THAT THERE'S SOME INCONSISTENCY BETWEEN THE EQUATIONS AND THE CODE PROVIDED IN THE EXERCISE IN TERMS OF NOTATION.
### The goal of the exercise is to come up with a good estimate of alpha_0, i.e. the coefficient of d_i, which is an endogenous
### variable, i.e. it is correlated with x'_i.
### z'_i are the instruments, that we use.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import statsmodels.api as sm
from statsmodels.api import OLS
from statsmodels.tools import add_constant
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LassoCV, Lasso
from sklearn.utils.testing import ignore_warnings
from sklearn.exceptions import ConvergenceWarning

### --------------------------------------------------------------------------- ###
### ----- JEG HAR IKKE NÅET AT LAVE EN JUPYTER NOTEBOOK MED RESULTATERNE, ----- ###
### -------------- SOM DU FORESLOG - JEG GØR DET NÆSTE GANG ------------------- ###
### --------------------------------------------------------------------------- ###

### ----- Ex. 6.1.1: Rewrite the below code to define a function simulate(n, m, k, plot), where plot is a boolean
### ----- indicating whether the density plot should be drawn or not. Your function should return all the matrices and
### ----- vectors required in the regression equations, including parameters and errors.

def simulate(n=1000, m=1500, k=10, plot=False):

    cov = 5
    # creating correlated errors - this is why we can't just use standard OLS, and use the IV model:
    errors = np.random.multivariate_normal(mean = [0,0], cov = [[cov, cov], [cov, cov]], size = n)

    # u (nu) and v (u) are correlated in this setup. Print out a density plot to see this, if plot=True
    if plot:
        h = sns.jointplot(errors[:,0], errors[:,1], kind = 'kde') # 'kde': Kernel Density Estimate
        h.set_axis_labels('$\\nu$', '$\epsilon$', fontsize=16)

    z = np.random.normal(size = (n,m))
    x = np.random.normal(size = (n,k))

    # Auxilliary equation
    nu = errors[:,0]
    Pi = np.array([5] + [x if np.random.uniform() > 0.9 else 0 for x in np.random.uniform(low = -2, high = 5, size = m - 1)])
    gamma = np.array([5] + [x if np.random.uniform() > 0.9 else 0 for x in np.random.uniform(low = -2, high = 5, size = k - 1)])

    d = z @ Pi + x @ gamma + nu
    # OBS: compared to the ex. description, nu=u and Pi=delta

    # Main equation
    u = errors[:,1]
    delta = np.array([5] + [x  if np.random.uniform() > 0.9 else 0 for x in np.random.uniform(low = -2, high = 5, size = k - 1)])
    alpha = np.random.uniform(1,2)

    y = alpha * d  + x @ delta + u
    # OBS: compared to the ex. description, u=v and delta=beta

    values = [y, d, x, z, u, nu, gamma, Pi, delta, alpha]
    var_names = ['y', 'd', 'x', 'z', 'u', 'nu', 'gamma', 'Pi', 'delta', 'alpha']

    return {'values': values, 'var_names': var_names}

simulated_variables = simulate(plot=False)


### ----- Ex. 6.1.2: Use your function to simulate a new dataset and regress the following OLS regression
### ----- y𝑖 ∼ 𝜋0 + 𝜋1𝑑𝑖 + 𝛾𝑖, where 𝛾𝑖 is a noise term.
### ----- Repeat this procedure 1000 times in a for loop and store the true  𝛼0  as well as the estimate  𝜋1  in two lists.
### ----- Plot a histogram of the differences  𝛼0−𝜋1 . What does this tell you about the regression you just ran?

ls_alpha =[]
ls_pi_1 = []
for i in range(0,1000):
    # simulate to create variables:
    simulated_variables = simulate()
    d = simulated_variables['values'][1]
    y = simulated_variables['values'][0]

    # generate noise term gamma_noise - confusing in the ex. description with different gammas
    gamma_noise = np.random.normal(0,1,len(d))

    # store true alpha in list:
    ls_alpha.append(simulated_variables['values'][-1]) # alpha is the last element in the simulated_variables object

    # create X object containing the constant, the variable d and the noise term:
    X = np.c_[d, gamma_noise]
    X = add_constant(X) # adds a column of ones - smart because the coefficient will be the intercept

    # setup model and fit
    model = OLS(y, X)
    results = model.fit()

    # store the pi_1 coeffient in list:
    ls_pi_1.append(results.params[1])

# diff between the real alpha and the estimated:
diff = list(np.array(ls_alpha) - np.array(ls_pi_1))

# histogram of the differences:
plt.hist(diff)

# The histogram reveals, that our estimation of alpha (pi_1) is a bit off - it's upwards biased.

### ----- 6.1.3: Knowing the DGP an obvious solution would be to run an IV regression, instrumenting  d𝑖  with  z𝑖 .
### ----- Unfortunately there are  m=1500  columns in  z𝑖  and only  n=1000  observations. Luckily, the way we have
### ----- simulated our data only a small subset of the  z𝑖 's actually influence  d𝑖 . The tricky part will be to pick
### ----- out the right  z𝑖 's.
### ----- To begin with simulate a new dataset and count the number of non-zero element in  Π  to verify that indeed
### ----- only very few  𝑧 's matter for  𝑑 .

# simulate new data set
simulated_variables = simulate(plot=False)
# find Pi
Pi = simulated_variables['values'][7]
# number of elements of Pi, that are not zero
np.count_nonzero(Pi) # around 150

### ----- Ex. 6.1.4: The ideal instrument for  𝑑𝑖  is exactly the  𝑧𝑖 's which have non-zero coefficients, multiplies by
### ----- the corresponding true simulated parameters in  𝛿0 . Having simulated the data ourselves, an easy way to compute
### ----- this is to simply calculate; 𝑑̂^(*) = z @ 𝛿0, where @ is the dot product. In reality we cannot get this ideal
### ----- instrument, because it would require regressing  𝑑𝑖  on all 500 variables with only 100 observations.
### ----- In a for loop over 1000 iterations, simulate new data, compute the ideal instrument 𝑑̂_i and regress the second
### ----- stage regression 𝑦𝑖 ~ 𝜋0 + 𝜋1 * 𝑑̂_i . Store the true  𝛼0  and the estimate  𝜋̂_1  in two lists. Finally draw a
### ----- histogram of the differences  𝛼0−𝜋̂ 1 . How does your histogram look this time, is this expected?

ls_pi_1 = []
ls_alpha = []

for i in range(0,1000):

    simulated_variables = simulate()

    z = simulated_variables['values'][3]
    Pi = simulated_variables['values'][7]
    y = simulated_variables['values'][0]

    # calculate ideal instrument
    ideal_d = z @ Pi

    # add constant term
    X = np.array(ideal_d)
    X = add_constant(X)

    model = OLS(y, X)
    results = model.fit()

    # store the pi_1 coeffient in list:
    ls_pi_1.append(results.params[1])

    # store true alpha in list:
    ls_alpha.append(simulated_variables['values'][-1]) # alpha is the last element in the simulated_variables object

# diff between the real alpha and the estimated:
diff = list(np.array(ls_alpha) - np.array(ls_pi_1))

# histogram of the differences:
plt.hist(diff)

# We can see from the histogram, that the differences between the real alpha and our estimations are distributed around
# 0. Only takes the relevant instruments into account.

### ----- Ex. 6.1.5: The below class implements post-lasso. A two step procedure where first a lasso model is used to
### ----- identify relevant parameters, and then OLS is used to estimate parameter values on the remaining variables.
### ----- Study the code, and understand as well as possible what is going on.

### ----- 1) What is stored in relevant_x?
# relevant_x stores the variables that are chosen by the Lasso model to be relevant + the variables specified to be
# included by the user + a constant.

### ----- 2) Why is the predict method so complicated?
# First return; if the user doesn't specify any X, we just predict on the relevant_x chosen by the Lasso in fit().
# Second return; if the user specifies a X, we check whether the X has the same dimensions as the variables used to fit(),
# i.e. relevant_x. If the dimensions are the same, we can use the specified X for predicting, otherwise not.
# Third return; if a X is specified, but the dimensions don't match, we use the variables in X, that is also contained
# in the relevant_x for the prediction.
# It is complicated because we want the user to able to specify an X, and that the dimensions have to match.


class PostLasso:
    def __init__(self, formula=None):
        self.lasso_model = Lasso()
        self.ols_model = None
        self.relevant_x = None
        self.subset_cols = None
        self.coefs = None
        self.formula = formula

    def __repr__(self):
        return f'PostLasso({self.formula})'

    @ignore_warnings(category=ConvergenceWarning)
    def fit(self, X, y, force_include_idx=None):
        ''' Estimate a model using Post-Lasso

        X: X matrix (without intercept)
        y: y vector
        force_include_idx: column indexes that ALWAYS is
            included in the OLS model, regardless of their
            status in the lasso stage.
        '''
        self.lasso_model = self.lasso_model.fit(X, y)
        self.coefs = np.insert(self.lasso_model.coef_, 0, self.lasso_model.intercept_) # inserts intercepts in the first col
        self.subset_cols = np.where(self.coefs != 0)[0] # select variables for which the coef after lasso is not zero
        if force_include_idx is not None: # add cols defined in force_include_idx to subset_cols
            self.subset_cols = np.union1d(self.subset_cols, force_include_idx)
        self.relevant_x = add_constant(X)[:, self.subset_cols] # add constant to X and choose only the subset cols
        self.ols_model = OLS(y, self.relevant_x).fit()
        return self

    def predict(self, X=None):
        ''' Predict using a fitted post-lasso model.
        '''
        if X is None:
            return self.ols_model.predict(self.relevant_x)
        if X.shape == self.relevant_x.shape:
            return self.ols_model.predict(X)
        return self.ols_model.predict(X[:, self.subset_cols])

### ----- Ex. 6.1.6: In this problem we will try to run through the post-lasso steps required to obtain an estimate of
### ----- 𝛼0 . Since we are doing this in python we will not be able to set the lasso hyperparameter optimally for this
### ----- kind of post-selection usage. There is a R package, developed especially to handle inference after
### ----- lasso-selection, which you should use in practise.
### -----For now, do the following steps 1000 times, storing the true  𝛼0  and estimate  𝛼0^ :

### ----- 0) Simulate a new dataset.
### ----- 1) Run a post-lasso regression of d on x and z,  d_𝑖 ~ x′_𝑖 𝛾 + z′_𝑖 𝛿 , forcing the inclusion of  x_𝑖  in the
### ----- OLS stage.

ls_alpha = []
ls_alpha_hat = []

for i in range(0,1000):

    simulated_variables = simulate()
    simulated_variables['var_names']
    x = simulated_variables['values'][2]
    d = simulated_variables['values'][1]
    z = simulated_variables['values'][3]
    y = simulated_variables['values'][0]
    X = np.c_[x,z]
    alpha = simulated_variables['values'][-1]


    # force include x:
    force_included_vars = [0,1,2,3,4,5,6,7,8,9]

    # setup the Post-Lasso model and fit
    post_lasso = PostLasso('di ~ xi + zi')
    post_lasso.fit(X,d, force_include_idx=force_included_vars)

    d_hat = post_lasso.predict()

### ----- 2) Run the second stage regression y𝑖 ~ 𝛼_0 𝑑̂_𝑖 + 𝛽 𝑥′𝑖 to recover 𝛼̂_0.
    X_2 = np.c_[x, d_hat]

    model = OLS(y,X_2)
    results = model.fit()

    alpha_hat = results.params[-1]

    #results.summary()

    ls_alpha.append(alpha)
    ls_alpha_hat.append(alpha_hat)


### ----- 3) How does this histogram compare to the naive one? How does it compare to the ideal one?

diff = list(np.array(ls_alpha) - np.array(ls_alpha_hat))

plt.hist(diff)

# The histogram is still a little biased, but close to the ideal one. It is without doubt way better than the naive.









