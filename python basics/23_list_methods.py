# methods in lists
# every specific data type has its own set of methods
# remember everything in python is an object

basket = [1, 2, 3, 4, 5]
# using append method which adds element at the end
# adding method
new_list = basket.append(100)
print(basket)
print(new_list) # it prints none here because append method returns none

# so in order to append we don't need to assign method to any variable
basket = [1, 2, 3, 4, 5]
basket.append(100)
print(basket) # it prints [1, 2, 3, 4, 5, 100]

# using insert method which adds element at particular index
# adding method
basket = [1, 2, 3, 4, 5]
new_list = basket.insert(0, 2300)
print(basket)
print(new_list) # it prints none here because insert method returns none

basket.insert(0, 2300)
print(basket) # it prints [2300, 1, 2, 3, 4, 5]

# using extend method
# it's basically an iterator
# adding method
basket = [1, 2, 3, 4, 5]
new_list = basket.extend([23,54]) # it's a no return method
print(basket)
print(new_list)

# removing method
# pop method
basket = [1, 2, 3, 4, 5]
new_list = basket.pop() # it's a return method and it removes the last element and is added to new_list
print(basket)
print(new_list)
# by default it removes the last element, but using .pop(index no) we can remove any element from list on particular index

# removing method
# remove method
basket = [1, 2, 3, 4, 5]
new_list = basket.remove(3) # it's a no return method and it takes particular element to be removed remember it doesn't accept index number
print(basket)
print(new_list)
print(type(basket[2])) # int type

# removing method
# clear method
basket = [1, 2, 3, 4, 5]
new_list = basket.clear() # it's a no return method and it removes all elements and show empty array like []
print(basket)
print(new_list)