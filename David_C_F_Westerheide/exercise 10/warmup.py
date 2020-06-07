from math import sqrt
import matplotlib.pyplot as plt

def pythagorian_triple(a,b,q):
    c2 = a**2 + b**2 
    qc2 = c2*q**2 
    qc2_new = (q*a)**2 + (q*b)**2
    if (qc2 == qc2_new):
        print('holds')
    else: 
        print('impossible error')

pythagorian_triple(3,4,2)

#I know that this was a bit silly. Real proof: 
# (qa)^2 + (qb)^2 = (qc)^2
# q^2 a^2 + q^2 b^2 = q^2 c^2
# Divide by q^2
# a^2 + b^2 = c^2     QED

A = []
B = []
for a in range(10000):
    for b in range(10000):
        A.append(a)
        B.append(b)

plt.scatter(A,B, s=0.5)
plt.xlabel('a')
plt.ylabel('b')
plt.title('Pythagorean Triples with a, b < 10000')
plt.show()
