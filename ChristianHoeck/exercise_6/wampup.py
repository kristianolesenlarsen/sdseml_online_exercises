def add(*args):
    result = 0
    for arg in args:
        result += arg
    return result

print(add(1,1))
print(add(1,1,1,-3))


# BONUS

def greet(**kwargs):
    greet_string = ""
    for key, value in kwargs.items():
        greet_string += f'{key} {value} and '
    greet_string = greet_string[:(len(greet_string) - len(" and "))]
    print(greet_string)


greet(hello="kristian", hi="Peter")