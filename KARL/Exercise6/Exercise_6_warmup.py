def add(*args):
    sum = 0
    for i in args:
        sum += i
    return sum

add(1,2,3,4)


def greet(hello=None, hi=None):
    ls_greetings = []
    if hello != None:
        ls_greetings.append('hello {}'.format(hello))
    if hi != None:
        ls_greetings.append('hi {}'.format(hi))

    string_greetings = " and ".join(ls_greetings) + "!"
    print(string_greetings)

greet(hello='Peter', hi='John')