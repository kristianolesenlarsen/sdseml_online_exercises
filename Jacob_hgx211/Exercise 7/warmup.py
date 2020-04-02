from random import uniform

def retry(n): 
    def wrapper(func): 
        for i in range(n):
            try:
                print(func())
            except:
                pass
        return func
    return wrapper
  
@retry(n = 5) 
def this_might_fail():
    c = uniform(0,1) > 0.8
    if c: return 'Success'
    raise ValueError('c too small')