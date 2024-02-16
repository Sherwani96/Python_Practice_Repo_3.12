my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

# difference method
# it says what is different my_set while comparing with your_set
# remember difference preference will be given to the first one
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
new_set = my_set.difference(your_set) # it's a return method
print(new_set) # it prints {1, 2, 3}
print(my_set) # it prints {1, 2, 3, 4, 5}, while my_set didn't change
print(your_set) # it prints {4, 5, 6, 7, 8, 9, 10}

# discard method
print("discard method")
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}

new_set = my_set.discard(3)  # discard method is a no return method
print(my_set) # it prints {1, 2, 4, 5}
print(new_set) # None

# difference_update method
# this method removes the common elements from first set which were common in both sets and update it
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
new_set = my_set.difference_update(your_set) # it's a non return method
print(my_set)  # it prints {1, 2, 3}, while my_set modified
print(your_set) # it prints {4, 5, 6, 7, 8, 9, 10}
print(new_set) # None

# intersection method
# it only prints the common elements without modifying the original
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
new_set = my_set.intersection(your_set) # it's a return method
new_set = my_set & your_set # can also use this
print(my_set)  # it prints {1, 2, 3, 4, 5}
print(your_set) # it prints {4, 5, 6, 7, 8, 9, 10}
print(new_set) # it prints {4, 5}

# isdisjoint method
# it checks if two sets are disjoint or not and returns true or false
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
new_set = my_set.isdisjoint(your_set) # it's a return method
print(my_set)  # it prints {1, 2, 3, 4, 5}
print(your_set) # it prints {4, 5, 6, 7, 8, 9, 10}
print(new_set) # it prints False
# it prints false here because they have common elements

# union method
# it combines elements from both sets and removes duplicates
my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
new_set = my_set.union(your_set) # it's a return method
new_set = my_set | your_set
print(my_set)  # it prints {1, 2, 3, 4, 5}
print(your_set) # it prints {4, 5, 6, 7, 8, 9, 10}
print(new_set) # it prints {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

# issubset method
# it checks if first set is subset of second set and returns true or false
# it can only return True if a first set totally resides in second set
my_set = {4, 5}
your_set = {4, 5, 6, 7, 8, 9, 10}
new_set = my_set.issubset(your_set) # it's a return method
print(my_set) # it prints {4, 5}
print(your_set) # it prints {4, 5, 6, 7, 8, 9, 10}
print(new_set) # it prints True

# issuperset method
# it can only ret
# return True when the second set possess all that elements that first set have
my_set = {4, 5, 6}
your_set = {4, 5, 6, 7, 8, 9, 10}
new_set = your_set.issubset(my_set) # it's a return method
print(my_set) # it prints {4, 5}
print(your_set) # it prints {4, 5, 6, 7, 8, 9, 10}
print(new_set)