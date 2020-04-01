from random import uniform

def retry(func, n):
    tries = 0
    while tries <= n:
        try:
            func()
            break
        except:
            tries += 1
            print("trying for the %d. time" % tries)


def this_might_fail():
    c = uniform(0,1) > 0.8
    if c: return  "Success"
    raise ValueError("c too small")

retry(this_might_fail, 20)