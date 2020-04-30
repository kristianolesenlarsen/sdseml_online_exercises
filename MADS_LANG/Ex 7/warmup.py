from random import uniform

def retry_n_times(n):
    def _decorator(fnc):
        def _wrapped():
            attempts = 0
            while attempts < n:
                try:
                    fnc()
                    print('success')
                    break
                except Exception as e:
                    attempts += 1
                    print(e)
        return _wrapped
    return _decorator

@retry_n_times(10)
def this_might_fail():
    c = uniform(0,1) > 0.8
    if c: return 'Success'
    raise ValueError('c to small')

this_might_fail()
