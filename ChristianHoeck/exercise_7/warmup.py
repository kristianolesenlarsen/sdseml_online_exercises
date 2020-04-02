## For some reason i could not just make a decorator which took agruments so a made a decorator factory instead.

def retry_factory(n=5):
    def decorator(function):
        def wrapper():
            for i in range(n):
                try:
                    result = function()
                    return result
                except:
                    print("Failed! Trying again")
        return wrapper
    return decorator

retry = retry_factory(6)

@retry
def this_might_fail():
    c = uniform(0,1) > 0.8
    if c: return 'Sucess'
    raise ValueError('c to small')
    
this_might_fail()
this_might_fail()