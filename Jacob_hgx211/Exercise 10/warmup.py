# QUESTION 1:
# Let (a,b,c) be a Pythagorean triple. Consider (q*a,q*b,q*c), where q is an
# integer. Then:
# (q*a)**2 + (q*b)**2 = (q*c)**2            <=>
# q**2 * a**2 + q**2 * b**2 = q**2 * c**2   <=>
# q**2(a**2 + b**2) = q**2 * c**2           <=>
# a**2 + b**2 = c**2.
# Thus, I have shown that if (a,b,c) is a Pythagoream triple, then
# (q*a,q*b,q*c) also is. In fact, I have shown the implication both ways:
# (a,b,c) Pythagorean triple <=> (q*a,q*b,q*c) Pythagorean triple



# QUESTION 2:
import matplotlib.pyplot as plt

N = 10000       # Limit on a,b (a,b < N)
triples = set() # Set for storing triples

# Generate Pythagorean triples with Euclid's formula (see Wikipedia for more).
# Euclid's formula: a = m**2 - n**2
#                   b = 2*m*n
#                   c = m**2 + n**2
#                   for m,n intergers with m>n.
# Since Euclid's formula only guarantees all non-primitive triples, I also use
# the result from question 1 to generate all primitive triples. This ensures
# that all triples are generated.
m = 2
n = 1
while m**2 - n**2 < N:
    n = 1
    while m > n and 2*m*n < N:
        a = m**2 - n**2
        b = 2*m*n
        c = m**2 + n**2
        q = 1
        while q*a < N and q*b < N:
            triples.add((q*a,q*b,q*c))
            triples.add((q*b,q*a,q*c))
            q += 1
        n += 1
    m += 1
    
# Graph all triples in (a,b) space
# pip install git+https://github.com/garrettj403/SciencePlots.git
plt.style.use('science')    
plt.figure(figsize=(8,6),dpi=400)
plt.scatter([triple[0] for triple in triples],
           [triple[1] for triple in triples], s=0.5)
plt.xlabel('a')
plt.ylabel('b')
plt.title('Pythagorean Triples, $a^2+b^2=c^2$', fontsize=20)
plt.xlim([0,N])
plt.ylim([0,N])
plt.gca().get_xaxis().set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.gca().get_yaxis().set_major_formatter(
        plt.FuncFormatter(lambda x, loc: "{:,}".format(int(x))))
plt.savefig('fig.png')