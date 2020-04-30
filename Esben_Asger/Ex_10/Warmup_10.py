# Warmup 10
import matplotlib.pylab as plt
#%matplotlib inline
from tqdm import tqdm
plt.style.use('ggplot')

# Def function that checks if a^2+b^2=c^2 s
def pytha(a,b,c):
    if (a**2+b**2==c**2) == True:
        return True
    elif (a**2+b**2)>c**2 == True:
        return 'small_c'
    elif (a**2+b**2)<c**2 == True:
        return 'big_c'

print(pytha(3,4,5))

# All pythagorean triples for a,b < 1000
# Hvis det gælder at pytha(qa,qb,qc)==True, hvis pytha(a,b,c)==True, kan man nemmere finde alle (a,b)<1000 --> overvej det 
a_list, b_list = [],[]
for a in tqdm(range(1, 100)):
    for b in range(a, 100): # b should not be smaller than a (obviously switching the values of a and b for a pytha-triple would be another pytha triple..but its not very informative)
        c = b
        while True: # c is always greater than b for pythagorean triples --> when a and b cannot be 0.
            if pytha(a,b,c)=='big_c': break # If c is too big, it doesn't make sense to keep on checking for greater values of c.
            if pytha(a,b,c)==True: a_list.append(a); b_list.append(b); break
            c += 1

plt.scatter(a_list, b_list)