import matplotlib.pyplot as plt


def TnFactory(n):
    if n == 0:
        def T(x):
            return 1
    elif n == 1:
        def T(x):
            return x
    else:
        def T(x):
            return 2*x*TnFactory(n-1)(x) - TnFactory(n-2)(x)
    return T

N = 5
for i in range(1,N+1):
    plt.plot(x, TnFactory(i)(x))


