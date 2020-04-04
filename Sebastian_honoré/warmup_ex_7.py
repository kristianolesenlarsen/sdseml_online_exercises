from random import uniform
from functools import wraps 

def this_might_fail():
    c = uniform(0,1) > 0.8
    if c: return "success"
    raise ValueError("c to small")

def retry(exceptions,n):
    def retry_decorator(f):
        @wraps(f)
        def f_retry(*args,**kwargs):
            iter=n
            while iter > 1:
                try:
                    return f(*args,**kwargs)
                    print("Succes")
                except exceptions as e:  
                    iter -=1
                    msg = str(f'Function:{f.__name__}\n'
                             f'Exception: {e}\n'
                            f'Retrying again')
        return f_retry
    return retry_decorator

@retry(ValueError,n=100)
def this_might_fail():
    c = uniform(0,1) > 0.8
    if c: return "success"
    raise ValueError("c to small")
