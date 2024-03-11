# zip
#  zip function works like a zipper

# example 01
a = [1, 2, 3]
b = [10, 20, 30]
c = ['a', 'b', 'c']

for item in zip(a, b, c):
    print(item)


# example 02
my_list = [1,2,3]
your_list = [10,20,30]

def multiply_by2(item):
    return item*2

def only_odd(item):
    return item % 2 != 0

print(list(zip(my_list, your_list)))

# it wraps the items in tuple
