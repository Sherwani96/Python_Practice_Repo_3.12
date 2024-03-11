from functools import reduce

my_list = [1,2,3]
your_list = [10,20,30]

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

def accumulate(acc, item):
    print(acc, item)
    return acc + item

print(reduce(accumulate, my_list, 0))      # can't use list with reduce function
                 # function  #iterable  #initial value
