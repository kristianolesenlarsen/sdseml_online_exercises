# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:56:49 2020

@author: tcg865
"""

import networkx as nx
import numpy as np
import pandas as pd

from scipy.special import binom
from triafun import fraction_triangles

url_base = 'http://www.sociopatterns.org/wp-content/uploads/2015/'

# edgelist
url_el = url_base + '07/High-School_data_2013.csv.gz'
col_names_el = ['timestamp', 'u1', 'u2', 'class1', 'class2']
el = pd.read_csv(url_el, header=None, names=col_names_el, delimiter=' ')

# individual characteristics
url_ind = url_base + '09/metadata_2013.txt'
col_names_ind = ['u', 'class', 'gender']
ind = pd.read_csv(url_ind, header=None, names=col_names_ind, delimiter='\t')\
            .set_index('u')

# remove observation with missing gender
has_gender = ind[ind.gender!='Unknown'].index

# DataFrames
ind = ind.loc[has_gender].copy()
el = el[el.u1.isin(has_gender) &  el.u2.isin(has_gender)].copy()

ind1 = ind
ind1['obs'] = 1

#n_class = ind1.groupby(['class','gender']).count()

Gdummies = pd.get_dummies(ind1['gender'])
ind1 = ind1.merge(Gdummies, left_index=True, right_index=True)

n_class = ind1.groupby('class').obs.count()
n_men = ind1.groupby('class').M.sum()
n_women = n_class-n_men

n_class = pd.DataFrame(n_class)
n_men   = pd.DataFrame(n_men)
n_women = pd.DataFrame(n_women)
# =============================================================================
# Ex. 13.1.1: Describe the edgelist columns content. Parse the timestamp. What 
# is the resolution of meetings? Use the parsed timestamp to count the meetings 
# by hour in local time.
# =============================================================================

# =============================================================================
# The first data set gives the contacts of the students of nine classes 
# during 5 days in Dec. 2013, as measured by the SocioPatterns infrastructure. 
# The file contains a tab-separated list representing the active contacts 
# during 20-second intervals of the data collection. Each line has the form 
# “t i j Ci Cj“, where i and j are the anonymous IDs of the persons in contact, 
# Ci and Cj are their classes, and the interval during which this contact
#  was active is [ t – 20s, t ]. If multiple contacts are active in a given 
#  interval, you will see multiple lines starting with the same value of t. 
#  Time is measured in seconds and expressed in UNIX ctime.
# =============================================================================

# =============================================================================
# Finally the metadata file contains a tab-separated list in which each line 
# of the form “i Ci Gi” gives class Ci and gender Gi of the person having ID i.
# =============================================================================



# =============================================================================
# Ex. 13.1.2: Count the number of meetings for each edge and save this as a 
# DataFrame called el_agg. Filter out edges with less than 5 minutes of 
# meetings. Attach the gender and class of both nodes.
# =============================================================================
ind.reset_index(level=0, inplace=True)
ind2 = ind.rename(columns={'gender':'gender2','class':'class2'})

el['meet_count']  = 1

agg = pd.DataFrame(el.groupby(['u1', 'u2']).sum()[['meet_count']])
agg.reset_index(inplace=True)

u1_agg = ind.merge(agg, left_on='u', right_on='u1')
u2_agg = ind.merge(agg, left_on='u', right_on='u2')
el_agg = pd.concat([u1_agg, u2_agg], ignore_index=True)
el_agg = el_agg.drop(columns={'u'}).rename(columns={'gender':'gender1','class':'class1'})
el_agg = el_agg.merge(ind2, left_on='u2', right_on='u')
el_agg = el_agg.drop(columns={'u'})
# =============================================================================
# el_agg = agg.merge(ind, left_on='u1', right_on='u')
# el_agg = el_agg.drop(columns={'u'})
# el_agg = el_agg.rename(columns={'class':'class1','gender':'gender1'})
# 
# el_agg = el_agg.merge(ind, left_on='u2', right_on='u')
# el_agg = el_agg.drop(columns={'u'})
# el_agg = el_agg.rename(columns={'class':'class2','gender':'gender2'})
# =============================================================================

el_agg['minutes_count'] = el_agg['meet_count'] * 1/3

el_agg['obs'] = 1

el_agg = el_agg[el_agg['minutes_count'] < 5]

# =============================================================================
# Ex. 13.1.3: Answer question in the function fraction_triangles below. Explain 
# how fraction_triangles is related to computing the clustering coefficient 
# (using nx.average_clustering).
# =============================================================================

# Fraction of triangles calculates how many triangles their exists in the 
# network divided by the maximum number of possible triangles (given by the 
# binomial coefficient). Hence, the fraction of triangles measures how 
# connected the nodes of the network are. If all nodes are connected the  
# fraction of triangles would equal unity.
# The clustering coefficient measures how many nodes a given node is linked to
# divided by the number of maximum possible nodes. The average clustering 
# coefficient is the averaged clustering coefficient of the network. Hence,
# if all nodes are connected the average clustering coefficient equals unity.

A  = np.array(
    [[0, 1, 1, 0],
     [1, 0, 1, 0],
     [1, 1, 0, 1],
     [0, 0, 1, 0]]
)

G = nx.from_numpy_array(A)
#nx.draw(G,with_labels=True)

def nth(A, n):
    A_ = A.copy()    
    for _ in range(1,n):
        A = A.dot(A_)
    return A

a_t = nth(A,3).diagonal().sum()/6
n = len(A[:,0])
p_t = binom(n, 3)

# =============================================================================
# Ex. 13.1.4: Apply the function fraction_triangles to el_agg and print the 
# triangle fraction in the network. Next remove all edges that go between 
# classes. Compute triangle fraction within each class and store it. Compute 
# the mean within class triangles and bootstrap the standard error of the mean. 
# Comment on the output
# =============================================================================

F=nx.from_pandas_edgelist(el_agg, 'u1', 'u2', edge_attr=True)

t = nx.triangles(F)
T = sum(t.values())/3
print("Number of triangles: ", T)

ft = fraction_triangles(el_agg, ind.u)

print("fraction of triangles: ", ft)

AC = nx.average_clustering(F)
print("clustering cofficient: ",AC)

el_agg_class = el_agg[el_agg['class1'] == el_agg['class2']]

tjeck = el_agg[el_agg['class1'] != el_agg['class2']]

counter = pd.DataFrame(ind.groupby(['class']).u.count())
counter.reset_index(level=0, inplace=True)
classes = counter.drop(columns={'u'})
classes = classes.rename(columns={'class':'classlist'})

from sklearn.utils import resample

list = classes.classlist.values.tolist()
length = len(list) 

class_ft = np.zeros((length,1))
obs      = np.zeros((length,1))


H   = pd.DataFrame(n_men.M/n_class.obs)
H.reset_index(level=0, inplace=True)
H = H.drop(columns={'class'})

B   = np.zeros((length,1))

MC = 10
mc_ft = np.zeros((length,MC))

for i in range(length): 
    
    class_agg   = el_agg_class[el_agg_class['class1'] == list[i]]
#    class_nodes = class_agg.groupby('class1') 
    class_nodes = class_agg.u1.unique()
    
    class_ft[i-1,0] = fraction_triangles(class_agg, class_nodes)
    
    n       = len(class_agg.class1)
    
#    nom     = (n_men[i]*(n_men[i]-1) + n_women[i]*(n_women[i]-1) ) / 2
#    denom   = n_class[i]*(n_class[i]-1)/2
    
    dum1 = pd.get_dummies(class_agg['gender1'])
    dum2 = pd.get_dummies(class_agg['gender2'])
    
    dumM =  pd.DataFrame(dum1.M*dum2.M)
    dumF =  pd.DataFrame(dum1.F*dum2.F)
    
    class_men = class_agg[class_agg['gender1']=='M']
    num_men     = len(class_men.class1)
            
    nom     = sum(dumM.M,0) #+ sum(dumF.F,0) 
    denom   = num_men
    
    B[i-1,0] = nom/denom
                  
#    print("class: ", list[i])
#    print("fraction of triangles: ", class_ft[i-1,0])
    
    for m in range(MC):
        
        mc_agg      = resample(class_agg, replace=True, n_samples=n, random_state=m*i) 
        mc_nodes    = mc_agg.groupby('class1') 
        
        mc_ft[i-1,m-1] = fraction_triangles(mc_agg, mc_nodes)    
 
dev = mc_ft - class_ft
std_error = pd.DataFrame(np.mean(dev*dev,axis=1))

class_ft    = pd.DataFrame(class_ft)
obs         = pd.DataFrame(obs)
B           = pd.DataFrame(B)

#B = B.rename(columns={'0':'obs'})

H           = pd.DataFrame(H)
IH          = (H.iloc[ : , 0 ] - B.iloc[ : , 0 ])/(1-B.iloc[ : , 0 ])


n_class.reset_index(level=0, inplace=True)
n_class = n_class.drop(columns={'class'})
n_men.reset_index(level=0, inplace=True)
n_men = n_men.drop(columns={'class'})

table = pd.concat([classes,n_class,n_men,class_ft,std_error,H,B,IH],1)
print(table)

# =============================================================================
# Ex. 13.1.5: Compute the inbreeding homophily for each class. Use the class 
# measures to compute the mean. Use a bootstrap to compute whether there is 
# inbreeding homophily.
# =============================================================================
