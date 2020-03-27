import requests
import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.datasets import make_classification

# Ex. 4.1.1
np.random.seed(seed=0)

N_SAMPLES = 1000
N_FEATURES = 5
GAMMA = 3
BETA = np.random.uniform(0,1, size = N_FEATURES, )

X = np.random.normal(size = (N_SAMPLES, N_FEATURES))
D = np.random.choice([0,1], size = N_SAMPLES)

X0  = np.random.normal(size = (N_SAMPLES))
v   = np.random.normal(size = (N_SAMPLES))

Y0      = X @ BETA + np.random.normal() # none-treatment outcome
Tau0    = (10/(1+np.exp(-GAMMA*X0))) * (1-D) # Deterministic treatment effect
Tau     = Tau0 + v # note that the error term v is common for both treated and none-treated
Y1      = Y0 + Tau # treament outcome;
y       = Y0 * D + Y1 * (1-D) # Observed outcome

plt.scatter(X0,y,marker='o',color='g',label='y')
plt.axhline(y=0, linewidth=1, color='k')
plt.xlabel('X0')
plt.ylabel('Output')
plt.legend(loc='upper left')
plt.title('scatter plot (observed outcome)')
plt.show()

# Ex. 4.1.2

# From the scatter plot below we see that the outcome when treated seems to 
# increase in X0. The outcome when not treated is non-increasing in X0, 
# since X0 has no effect when no treatment, D=1 
plt.scatter(X0,Y1,marker='o',color='r',label='Y1')
plt.scatter(X0,Y0,marker='o',color='b',label='Y0')
#plt.scatter(X0,y,marker='x',color='g')
plt.axhline(y=0, linewidth=1, color='k')
plt.xlabel('X0')
plt.ylabel('Output')
plt.legend(loc='upper left')
plt.title('scatter plot (counter factual outcome)')
plt.show()

X0D     = X0[D==0]
TauD    = Tau[D==0]
Tau0D   = Tau0[D==0]

# Due to the functional form of the treatment, the expected treatment effect 
# goes to zero when X0 goes to minus infinity and the expected treatment 
# effect goes to ten when X0 goes to infinity.
plt.plot(X0D,TauD,'o',label='Tau')
plt.plot(X0D,Tau0D,'o',label='Tau0')
plt.axhline(y=0, linewidth=1, color='k')
plt.xlabel('X0')
plt.ylabel('treatment')
plt.legend(loc='upper left')
plt.title('scatter plot (treatment effect)')
plt.show()

# Ex 4.1.3

# The specified model for estimation is miss-specified since, the model
# assumes that the treatment effect is constant ( delta*T ) and independent of 
# X0. Alternatively we could assume that the treatment is linear function of X0 
# ( (delta_1 + delta_2*X0)*T ). However, we will still be considering a 
# miss-specified model
import statsmodels.api as sm
a  = np.ones(N_SAMPLES)
T  = 1-D
X_ols = np.vstack((T, a, X[:,0], X[:,1], X[:,2], X[:,3], X[:,4])).T

Treaded = T[T==1]

linear      = sm.OLS(y,X_ols)
results     = linear.fit()
par_ols     = results.params
pred_ols    = linear.predict(par_ols, X_ols)
print('')
print('Average treament effect: ',np.mean(Y1[T==1]-Y0[T==1]))
print('Estimated expected treatment effect:',pred_ols[0]) 

plt.plot(X0,y,'o',color='g',label='y')
plt.plot(X0,pred_ols,'x',color='k',label='pred')
plt.axhline(y=0, linewidth=1, color='k')
plt.xlabel('X0')
plt.ylabel('outcome')
plt.legend(loc='upper left')
plt.title('scatter plot (predicts)')
plt.show()

X0T = X0*T
X_bonus = np.vstack((T, X0T, a, X[:,0], X[:,1], X[:,2], X[:,3], X[:,4])).T

linear_bonus    = sm.OLS(y,X_bonus)
results_bonus   = linear_bonus.fit()
par_bonus       = results_bonus.params
pred_bonus      = linear_bonus.predict(par_bonus, X_bonus)

print('Estimated expected treatment effect (bonus):',pred_bonus[0]) 

plt.plot(X0,y,'o',color='g',label='y')
plt.plot(X0,pred_bonus,'x',color='k',label='pred, bonus')
plt.axhline(y=0, linewidth=1, color='k')
plt.xlabel('X0')
plt.ylabel('outcome')
plt.legend(loc='upper left')
plt.title('scatter plot (predicts, bonus)')
plt.show()

delta = Y1-Y0
delta_sort = np.sort(delta[T==1])

data_raw = pd.DataFrame({'D': D, 'X0': X0, 'X1': X[:,0], 'X2': X[:,1], 'X3': X[:,2], 'X4': X[:,3], 'X5': X[:,4], 'y': y, 'Y0': Y0, 'Y1': Y1})

data_raw.to_csv(r'C:\Users\tcg865\Dropbox\PhD\Courses\Machin learning\session5\export_dataframe.csv', index = False, header=True)


param_ols = pd.DataFrame({'par': par_ols})
param_ols.to_csv(r'C:\Users\tcg865\Dropbox\PhD\Courses\Machin learning\session5\param_ols.csv', index = False, header=True)

param_bonus = pd.DataFrame({'par': par_bonus})
param_bonus.to_csv(r'C:\Users\tcg865\Dropbox\PhD\Courses\Machin learning\session5\param_bonus.csv', index = False, header=True)
