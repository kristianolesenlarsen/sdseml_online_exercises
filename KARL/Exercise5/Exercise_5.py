# Session 5: The Generalized Random Forest

# Causal forests
# Random forest: Bootstrap sample; used for both partitioning and estimating mean(x)
# Double Sample Trees: Subsample for partition (J), subsample for mean (I)

import requests
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification
from statsmodels.formula.api import ols
import sys
#sys.modules[__name__].__dict__.clear()


### ----- Ex. 5.1.1.: Complete the code below to simulate data according to (
### 𝑇=𝑈(0,1)>0.5
### 𝑌(𝑇=0)=𝑋𝛽+𝜖
### 𝜏(𝑋)={10/(1+𝑒−𝛾𝑋0)+𝜈 for 𝐷=0, 𝜈 for 𝐷=1
### 𝑌(𝑇=1)=𝑌(0)+𝜏(𝑋)

N_SAMPLES = 10000
N_FEATURES = 5
GAMMA = 3
BETA = np.random.uniform(0,1, size = N_FEATURES)

X = np.random.normal(size = (N_SAMPLES, N_FEATURES))
X0 = X[:,0]
D = np.random.choice([0,1], size = N_SAMPLES)
T = np.array(np.random.uniform(0,1, size = N_SAMPLES) > 0.5).astype(int) # generate array of random integers 0 or 1

Y0 = X @ BETA + np.random.normal() # @ is the dot product operator
# Now we calculate Tau, the treatment effect. Important to point out: The numerator is 10 when D=0 and 0 when D=1 - this satisfies
# the conditions outlined above:
Tau = 10*(1-D)/(1+np.exp(-GAMMA*X0)) + np.random.normal(size=N_SAMPLES)
Y1 = Y0 + Tau # Y1 is the baseline Y0 plus the treatment effect Tau.
# y is the observed y.
y = Y0 + T*(Y1 - Y0) # remember T is either 1 or 0, so y becomes Y1 for T=1 and Y0 for T=0.

### ----- Ex. 4.1.2: Create a two-subplot figure, and plot 𝑌(0) and 𝑌(1) in one subplot against 𝑋0. Plot 𝜏(𝑥) against
### ----- 𝑋0 in the other subplot. What do you see? Why do we observe 𝜏=0 in many cases?

# create figure with two subplots:
fig, ax = plt.subplots(1,2, figsize = [12,6])

# subplot 1, plotting Y0 and Y1 against X0:
ax[0].scatter(X0, Y0, label='$Y(0)$')
ax[0].scatter(X0, Y1, label='$Y(1)$')
# add visual stuff to subplot 1:
ax[0].set_xlabel('$X_0$')
ax[0].set_ylabel('$Y(T)$')
ax[0].legend()
ax[0].grid(True)

# subplot 2, plotting tau against X0
ax[1].scatter(X0, Tau, label ='\tau(x)')
# add visual stuff to subplot 2:
ax[1].set_xlabel('$X_0$')
ax[1].set_ylabel('$\\tau(x)$') # \\ to access special character
ax[1].grid(True)

# add 'titles' to each subplot, A & B:
fig.text(0.05, 0.85, 'A', fontsize=24, fontweight = 'bold')
fig.text(0.51, 0.85, 'B', fontsize=24, fontweight = 'bold')

# Conclusion: for half of the samples Y0 and Y1 are located in the same area and for the other half Y1 tends to increase when
# X0 increases. This is because the treatment effect depends on the value of D, which can be either 0 or 1. When it is 0, the
# treatment effect is just noise. When it is 1 the treatment effect is positively correlated with X0.

### ----- Ex. 5.1.3: Import statsmodels and estimate a simple linear regression:

df = pd.concat(
    [
        pd.DataFrame(X, columns=['X{}'.format(i) for i in range(N_FEATURES)]),
        pd.DataFrame(T, columns=['T']),
        pd.DataFrame(y, columns=['y'])

    ],
axis = 1) # concat the dataframes horizontally

# set up the model and estimate:
model = ols('y ~ T + X0 + X1 + X2 + X3 + X4', df)
res = model.fit()
res.summary()

## 1) What is your estimate of  𝛿̂ 0 ?
# The coefficient to T is estimated to be 2.54 and statistically significant.

## 2) How does this number fit with the figures you drew in the previous exercise?
# It fits well with the figures. delta must be the average treatment effect since, T is a binary variable that equals 1 if treated
# and 0 if not treated. From the second subplot we see that for the 50% being treated (i.e. the diagonal) the treatment effect
# seems to vary between 0 and 10, which makes good sense taking our definition of tau into account. So assuming that the treatment
# effect are evenly distibuted in this range, the average will be 5. This is half of the datapoint, the treatment effect of the
# other half is just noise, so zero mean. The mean treatment effect of the entire samples must therefore be around 2,5.

# Do you have any suggestions for improving the estimate of the model, comment on whether your improvements would provide unbiased estimates of  𝜏 ?
# ...

### ----- Ex. 4.1.4: For this question we will need to move into R (or use rpy2). If you are working in python you can skip this
### ----- step, otherwise do the following: Save a dataframe, containing  𝑋 ,  𝑦 ,  𝑇 , and  𝐷  as a csv file on your computer.

df = pd.concat([df, pd.DataFrame(D, columns=['D'])], axis=1)

df.to_csv('/Users/karlbindslev/Documents/Studie/SDS_Econometrics_ML/Exercises/Ex5_export_to_R.csv', index = False)


### ----- Ex. 4.1.5 a: Open up R and read the data you just saved into a dataframe(or work in rpy2). Install and load the two
### ----- libraries tidyverse and grf.

# Done in R.

### ----- Ex. 4.1.5 b: Copy the following code into R to split your dataframe into two matrices, X, and y. Implement the exact
### ----- same procedure to create a third matrix W which contains the treatment indicator (Note T is a reserved name in R, so
### ----- name your third matrix W).

# Done i R.

### ----- Ex. 4.1.6 a: Estimate a causal forest model using the GRF package, and store the result in a new variable cf. Then use
### ----- the following line to create a dataframe of predicted treatment effects on the same data that you trained the model on.

# Done in R.

### ----- Ex. 4.1.6 b: This concludes our venture into R. Now load the treatment effects into a pandas dataframe, and plot a
### ----- scatterplot of the estimated individual treatment effects against the simulated "true" ITE's Tau that you produced in
### ----- the beginning of this exercise set.

df = pd.read_csv('/Users/karlbindslev/Documents/Studie/SDS_Econometrics_ML/Exercises/individual_treatment_effects.csv')

plt.scatter(df['predictions'], Tau)

