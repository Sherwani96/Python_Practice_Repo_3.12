# sets

# sets are unordered collections of data or unique objects
#  sets are enclosed in curly braces {}
# set objects does not support indexing
# we can only check the item that it exists or not using in operator

my_set = {1, 2, 3, 4, 5}
# in sets there is no duplicate data
my_set = {1, 2, 3, 4, 5, 5}
print(my_set)
# it's going to eliminate the repetitive data in the set and print {1, 2, 3, 4, 5}

# add method
my_set = {1, 2, 3, 4, 5}
my_set.add(61)
print(my_set) # it prints {1, 2, 3, 4, 5, 61}

# changing a list into a set
my_list = [1, 2, 3, 4, 5]
# using set method
my_set = set(my_list)
print(my_set) # it prints {1, 2, 3, 4, 5}

# using in operator
my_set = {1, 2, 3, 4, 5}
print(3 in my_set) # it prints True

# we can use len function to find the length of set
# we can also convert a set into list using list method
my_set = {1, 2, 3, 4, 5}
print(list(my_set)) # it prints [1, 2, 3, 4, 5]

# copy method
my_set = {1, 2, 3, 4, 5}
new_set = my_set.copy()

# clear method
my_set = {1, 2, 3, 4, 5}
new_set = my_set.clear() # it's a return method
print(my_set) # it prints set()
print(new_set) # it prints None