def add(*nums): return sum(nums)

def greet(**kwargs):
    greets = list(kwargs.keys())
    names = list(kwargs.values())
    to_print = ''
    
    for i in range(len(greets)):
        to_print = to_print + greets[i] + ' ' + names[i]
        if i == len(greets) - 1:
            to_print = to_print + '!'
        elif i == len(greets) - 2:
            to_print = to_print + ' and '
        else:
            to_print = to_print + ', '
    
    return to_print