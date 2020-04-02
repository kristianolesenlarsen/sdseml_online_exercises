def add(*args):
    return sum(args)

def greet(hello, hi = ""):
    if hi == "":
        return f'hello {hello}'
    
    elif hi != "":
        return f'hello {hello} and hi {hi}'