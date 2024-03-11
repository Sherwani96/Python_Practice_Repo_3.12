from functools import reduce
# lambda expressions
# lambda is computer programming world and is compatible with functional programming
# lambda functions in python are anonymous functions, and don't need more than once.
# they don't have name


# body of lambda function
# lambda param: action(param)

my_list = [1,2,3]

def accumulate(acc, item):
    print(acc, item)
    return acc + item

print(list(map(lambda item: item*2, my_list)))              # multiply by 2
print(list(filter(lambda item: item % 2 != 0, my_list)))    # filter odd numbers
print(reduce(lambda acc, item: acc + item, my_list))