# functions we consider in functional programming paradigm
# map, filter, zip and reduce

# map

# map is a function that takes a function as an argument, and second argument will be an iterables

def multiply_by_2(item):
    return item * 2

print(list(map(multiply_by_2, [1,2,3])))  # in order to see the output we need to convert it into list
# map function already produce a list of items by iterating each item from the list, and make a new list of items

# another way
my_list = [1,2,3]
def multiply_by_2(item):
    return item * 2

print(list(map(multiply_by_2, my_list)))
print(my_list) # it will not change the original list, because map function does not alter the original list, it makes new list for