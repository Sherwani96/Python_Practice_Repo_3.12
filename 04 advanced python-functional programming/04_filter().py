# filter

my_list = [1,2,3]
def multiply_by_2(item):
    return item * 2

def only_odd(item):
    return item % 2 != 0

print(list(filter(only_odd, my_list)))     # it takes a function as an argument and 2nd argument is iterables
print(my_list)
