from random import uniform

def retry(n):
    def wrapper(func):
        for i in range(n):
            try:
                print(func())
                break
            except Exception as e:
                print(e)
        return func
    return wrapper

@retry(5)
def this_might_fail():
    c = uniform(0, 1) > 0.8
    if c: return "Success"
    raise ValueError('c to small')