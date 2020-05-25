# Import python packages

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statsmodels.api as sm
import statsmodels.formula.api as smf

# Import simulated data into a pandas DataFrame

data = pd.read_csv('peer_effects_room.txt')
data = pd.DataFrame(data)

# Ex. 12.1.1: Create a column called person_other with identity of the other person in room

room1 = data.groupby('room').person.max()
room1 = pd.DataFrame(room1)
room1 = room1.rename(columns={'person':'person_max'})

room2 = data.groupby('room').person.min()
room2 = pd.DataFrame(room2)
room2 = room2.rename(columns={'person':'person_min'})

data_new = data.merge(room1, left_on='room', right_index=True)
data_new = data_new.merge(room2, left_on='room', right_index=True)

def f(row):
    if row['person'] == row['person_max']:
        val = row['person_min']
    else:
        val = row['person_max']
    return val

data_new['person_other'] = data_new.apply(f, axis=1)

data_other = data.rename(columns={'high_school_GPA':'high_school_GPA_other',
                                  'college_GPA':'college_GPA_other',
                                  'person':'personA'}
                ).drop(columns='room')
    
data_new = data_new.merge(data_other, left_on='person_other', right_on='personA')

data_new = data_new.drop(columns={'personA','person_min','person_max'})

# Ex. 12.1.2: Add information on the roommate GPA in high school and college.

y = data_new['college_GPA']
X1 = data_new['high_school_GPA']
X1 = sm.add_constant(X1)

olsmod1     = sm.OLS(y,X1)
results1     = olsmod1.fit()
print(results1.summary())

ypred1 = results1.predict(X1)

plt.plot(data_new['high_school_GPA'], data_new['college_GPA'], 'o', color='black')
plt.plot(data_new['high_school_GPA'], ypred1, color='red')

plt.xlabel('High school GPA')
plt.ylabel('College GPA')
plt.title('Scatter plot')

plt.show()

# Ex. 12.1.4: Plot high school GPA vs roommate's high school GPA. Comment on 
# the output. Run a regresion of high school GPA on roommate's high school GPA 
# to formally check random assignment.

X2 = data_new['high_school_GPA_other']
X2 = sm.add_constant(X2)

y2          = data_new['high_school_GPA']
olsmod2     = sm.OLS(y2,X2)
results2    = olsmod2.fit()
print(results2.summary())

ypred2 = results2.predict(X2)

plt.plot(data_new['high_school_GPA_other'], data_new['high_school_GPA'], 'o', color='black')
plt.plot(data_new['high_school_GPA'], ypred2, color='red')

plt.xlabel('High school GPA')
plt.ylabel('High school GPA room mate')
plt.title('Scatter plot')

plt.show()

# Ex. 12.1.5: Plot own GPA in college vs. roommate GPA in high school. Comment 
# on the output. Test whether there is an impact using a regresion of college 
# school GPA on high school GPA for the person itself and its roommate.

N = data_new.shape[0]
c = np.ones((N, 1))
X3 = data_new[['high_school_GPA','high_school_GPA_other']]
X3 = sm.add_constant(X3)
olsmod3  = sm.OLS(y,X3)
results = olsmod3.fit()
print(results.summary())

ypred3 = results.predict(X3)

plt.plot(data_new['high_school_GPA'], data_new['high_school_GPA_other'], 'o', color='black')

plt.xlabel('College GPA of room mate')
plt.ylabel('College GPA')
plt.title('Scatter plot')

plt.show()

