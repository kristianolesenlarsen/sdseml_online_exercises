import numpy as np
import pandas as pd

X = [1]

def TnFactory(n):
    for x in X:
        if n == 0:
            return 1
        elif n == 1:
            return x
        else:
            return 2*TnFactory(n-1) - TnFactory(n-2)



TnFactory(5)

#This does not work