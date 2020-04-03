from functools import wraps
from random import uniform

def retry(n):
    def retry_decorator(func):
        @wraps(func)
        def wrapper():
            for i in range(n - 1):
                try: 
                    func()
                    return
                except: pass
            func()
                    
        return wrapper
    
    return retry_decorator

@retry(n=10)
def this_might_fail():
    c = uniform(0,1) > 0.8
    if c: return print('Success')
    raise ValueError('c too small')

this_might_fail()