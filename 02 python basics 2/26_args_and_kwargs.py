# *args and **kwargs

def super_func(*args):   # for multiple args we use * before the args
    print(*args) # if used * it will just show the args, if not it will show the tuple of args
    return sum(args)

print(super_func(1, 2, 3, 4, 5))

def super_func(name, *args, i = 'hi', **kwargs):   # for multiple args we use * before the args, for multiple kwargs we use ** before the kwargs
    total = 0
    for items in kwargs.values():  # it shows dictionary for kwargs used in this for loop to take out each item from it
        total += items
    return sum(args) + total

print(super_func('salman', 1, 2, 3, 4, 5, num3 =45, num4 = 55))

# rules of using parameters in the function or the sequence of parameters
# Rule = params, *args, default parameters, **kwargs