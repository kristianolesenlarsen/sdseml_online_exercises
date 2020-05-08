### --------------------------------------------------- ###
### ----- Warm-up week 11: Chebychevs polynomials ----- ###
### --------------------------------------------------- ###

# Fails in cases where n>1?

def TnFactory(n):

    if n == 0:
        def T_n(x):
            return 1
    elif n == 1:
        def T_n(x):
            return x
    else:
        def T_n(x):
            return 2*x*TnFactory(n-1) - TnFactory(n-2)
    return T_n

T_0 = TnFactory(0)
T_0(1)
T_0(2)

T_1 = TnFactory(1)
T_1(1)
T_1(2)

T_3 = TnFactory(3)
T_3(1)
T_3(2)