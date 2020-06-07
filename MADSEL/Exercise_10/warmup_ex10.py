import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def pythagoras(n):
    A = []
    B = []
    for b in range(n):
        for a in range(1,b):
            c = np.sqrt(a*a+b*b)
            if c % 1 == 0:              #only whole numbers - no decimals
                print(a,b, int(c))
                A.append(a)
                B.append(b)
    return A,B
A, B = pythagoras(10000)

plt.scatter(A,B,s=0.2)


