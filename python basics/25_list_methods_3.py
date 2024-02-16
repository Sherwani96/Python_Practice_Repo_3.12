
# using sort method
# sort method alters the original list
basket = ['a', 'b', 'c', 'd', 'e', 'd']   # it sorts the list in alphabetical order
new_list = basket.sort()  # it's a no return method
print(basket)
print(new_list)

# using sorted function
basket = ['x', 'a', 'b', 'c', 'd', 'e', 'd']  # sorted function does not later the original list but creates a new list
new_list = sorted(basket)  # it's a return function
print(basket)
print(new_list)

# copy method can also be used to copy a list

# reverse method
basket = ['a', 'b', 'c', 'd', 'e', 'd']  # it brings the list in reverse order
new_list = basket.reverse()  # it's a no return method
print(basket)
print(new_list)