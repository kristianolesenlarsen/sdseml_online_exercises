import progressbar

t = (3,4,5)
def pythagoras(tup):
    return tup[2]**2 == tup[0]**2 + tup[1]**2
pythagoras(t)


a_s,b_s = [],[]
for a in progressbar.progressbar(range(1,200)):
    for b in range(1,200):
        for c in range(1,200):
            if pythagoras((a,b,c)) == True:
                a_s.append(a)
                b_s.append(b)

plt.scatter(a_s,b_s, s=10)
