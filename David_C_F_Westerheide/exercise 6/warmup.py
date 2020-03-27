
def  add(*varargs):
    return sum(varargs)

print(add(1,1,1,1,1,1))

def greet(**varargs):
    narg= len(varargs.items())
    if narg == 1:
        for greeting, name in varargs.items(): 
            print("%s %s!" % (greeting,name))
    else:
        g = ""
        for greeting, name in varargs.items(): 
            g = g + "%s %s and " % (greeting, name) 
        g = g[:-5]+"!"
        print(g)
        
greet(Hallo="David")
greet(Hello="Kristian", hi="Peter")
greet(Hello="Kristian", hi="Peter", hej="Anders")
