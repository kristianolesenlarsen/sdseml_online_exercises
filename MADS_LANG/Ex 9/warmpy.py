import numpy as np
from scipy import integrate
import matplotlib.pyplot as plt
import math
%matplotlib inline
from publib import set_style, fix_style

set_style(['origin','latex']) # the style sheet is from https://github.com/erwanp/publib

def Integrate(f, a, b):
        I, _ = integrate.quad(f, a, b)
        return I


f = lambda x : 1/(math.log(x))

fig, ax = plt.subplots(figsize=(16,6))
Ns = np.linspace(10,10**10,100)
Is = [Integrate(f,n,2) for n in Ns]
ax.plot(Ns,Is, label="Li(n)")

ax.legend(bbox_to_anchor=(1.2, 1))
fix_style(['origin', 'latex'])
