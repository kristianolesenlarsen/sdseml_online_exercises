# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
#1. n_estimators are the trees you build in the decision tree. The higher number of n_estimators enusres the perfomance of the code and give stronger predictions.-
# However, the n_estimators include diminishing returns and thus comes with a computational risk you should therefor tune as high af value as the processor can handle.
#2. max_depth is the maximum depth of the tree. The deeper the tree the more complex the decisions get, and could result in overfitting the model making it useless in real applications.
#If there max_depth is set to "None" then nodes are expanded until all leaves are pure or until the all leaves contain less than the 
#minimum_sample_split samples which is the minimum number of samples required to split an internal node.
#3. max_features is the number of features to consider when looking for the best split. The max_features is set up as an if/then construction.
#By specifying enough max_features you will obtain a better chance of finding the best split. Max_features can however increase the correlation and thus increase varitaion of the model.
#4. Bootstrap is a boolean varible (True/False) and is used to pick out the dataset. If False, the whole dataset is used to build each tree. 

##2
import pandas as pd
from sklearn.datasets import load_wine
from sklearn.datasets import load_digits

get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pylab as plt
from sklearn.preprocessing import StandardScaler

from umap import UMAP
from sklearn.manifold import TSNE
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis as LDA

# Wine data
data_wine = load_wine()
X_wine = data_wine['data']
y_wine = data_wine['target']

# Digits data
data_digits = load_digits()
X_digits = data_digits['data']
y_digits = data_digits['target']

from sklearn.preprocessing import StandardScaler
import numpy as np


#For digits

PCAx = PCA().fit_transform(X_digits,y_digits)
    
LDAx = LDA().fit_transform(X_digits,y_digits)
    
tSNEx = TSNE().fit_transform(X_digits,y_digits)
    
umapx = UMAP().fit_transform(X_digits,y_digits)

#Plot for digits

fig = plt.figure(figsize=(10,10))
fig.suptitle("Digits")
plt.subplot(2,2,1)
plt.scatter(PCAx[:,0], PCAx[:,1], c=y_digits, cmap='viridis')
plt.title("Principal Component Analysis", fontsize=10)

plt.subplot(2,2,2)
plt.scatter(LDAx[:,0], LDAx[:,1], c=y_digits, cmap='viridis')
plt.title("Linear Discriminant Analysis", fontsize=10)

plt.subplot(2,2,3)
plt.scatter(tSNEx[:,0], tSNEx[:,1], c=y_digits, cmap='viridis')
plt.title("t-Distributed Stochastic Neighbor Embedding", fontsize=10)

plt.subplot(2,2,4)
plt.scatter(umapx[:,0], umapx[:,1], c=y_digits, cmap='viridis')
plt.title("Uniform Manifold Approximation and Projections", fontsize=10)

plt.show()


#For wine

# Standardize features by removing mean and scale to unit variance. Features will center at origin.
sc = StandardScaler()
X_std_wine = sc.fit_transform(X_wine)

# create covariance matrix. Could also use correlation matrix
cov_mat = np.cov(X_std_wine.T)

# create eigenvectors and eigen values to find PC1 and PC2:
eigen_vals, eigen_vecs = np.linalg.eig(cov_mat)

# Sort the eigenvalues by decreasing order to rank eigenvectors 
eigen_vals, eigen_vecs = zip(*sorted(
    zip(abs(eigen_vals), eigen_vecs.T),
    key=lambda kv: kv[0], reverse=True
))

# Get the top 2 eigenvectors
top_k_eigen_vecs = eigen_vecs[:2]

# Compose basis transformation matrix
W = np.hstack([
    w.reshape(-1, 1) for w in top_k_eigen_vecs
])

# Transform datapoints
Z = np.dot(X_std_wine, W)

PCAw = PCA().fit_transform(Z)
    
LDAw = LDA().fit_transform(Z, y_wine)
    
tSNEw = TSNE().fit_transform(Z)
    
umapw = UMAP().fit_transform(Z)

#Plot for wine using the standardized values

fig = plt.figure(figsize=(10,10))
fig.suptitle("Wine")
plt.subplot(2,2,1)
plt.scatter(PCAw[:,0], PCAw[:,1], c=y_wine, cmap='viridis')
plt.title("Principal Component Analysis", fontsize=10)

plt.subplot(2,2,2)
plt.scatter(LDAw[:,0], LDAw[:,1], c=y_wine, cmap='viridis')
plt.title("Linear Discriminant Analysis", fontsize=10)

plt.subplot(2,2,3)
plt.scatter(tSNEw[:,0], tSNEw[:,1], c=y_wine, cmap='viridis')
plt.title("t-Distributed Stochastic Neighbor Embedding", fontsize=10)

plt.subplot(2,2,4)
plt.scatter(umapw[:,0], umapw[:,1], c=y_wine, cmap='viridis')
plt.title("Uniform Manifold Approximation and Projections", fontsize=10)

plt.show()


# %%


