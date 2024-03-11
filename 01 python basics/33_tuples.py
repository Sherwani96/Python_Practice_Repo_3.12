# tuples
# tuples are like list but they are immutable or unchangeable
# but it is enclosed in () paranthesis

my_tuple = (1 , 2, 3, 4, 5)
# my_tuple[0] = 22 # TypeError: 'tuple' object does not support item assignment
print(my_tuple)

# tuple unpacking
# you can access items in tuple using index method
print(my_tuple[3]) # 4

# using in method
print(1 in my_tuple) # True

# using slicing
my_tuple = (1 , 2, 3, 4, 5)
new_tuple = my_tuple[1:3]  # (2, 3)
print(new_tuple)

# assigning values of tuple to multiple variables
a,b,c, *rest = (1 , 2, 3, 4, 5, 6)
print(a) # 1
print(b) # 2
print(c) # 3
print(rest) # [4, 5, 6]
print(type(rest)) # <class 'list'>
print(type(a))  # <class 'int'>

# tuples have only two methods

# count method
my_tuple = (1 , 2, 3, 4, 5, 5, 5)
new_tuple = my_tuple.count(5) # 3 , it's a return method
print(my_tuple)
print(new_tuple) # 3
# count method counts how many times an item is present in tuple

# index method
my_tuple = (1 , 2, 3, 4, 5, 5, 5)
new_tuple = my_tuple.index(5)
print(my_tuple)
print(new_tuple) # 4
# we can also use start and stop sequence with index method if there many repeated items

# we can also use len method to find the len of tuple
