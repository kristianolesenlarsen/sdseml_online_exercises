import matplotlib.pylab as plt

#a^2 + b^2 = c^2
#    (qa)^2 + (qb)^2 = (qc)^2 
#<=> q^2*a^2 + q^2*b^2 = q^2*c^2
#dividing by q^2:
#<=> a^2 + b^2 = c^2
#Q.E.D.

def is_triple(a, b, c):
     return a**2+b**2 == c**2
    
A = []
B = []

for a in range(1, 200):
    for b in range(1, 200):
        for c in range(1, 200):
            if is_triple(a, b, c):
                A.append(a)
                B.append(b)
                
plt.scatter(A,B, s=10)