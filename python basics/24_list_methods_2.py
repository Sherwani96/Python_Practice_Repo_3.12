
basket = ['a', 'b', 'c', 'd', 'e']
new_list = basket.index('c')  # here .index() method will return the index of 'c' so it's a return method
print(basket)
print(new_list)

# using index method with start and stop
basket = ['a', 'b', 'c', 'd', 'e']
new_list = basket.index('d', 0, 4)
print(basket)              #start^ stop^
print(new_list)

# to check the item is in the list or not
basket = ['a', 'b', 'c', 'd', 'e']
new_list = 'c' in basket  # it's a return method
print(new_list)  # it will return True

# count method
basket = ['a', 'b', 'c', 'd', 'e', 'a']
# it tells how many times the item is in the list or the no of occurrences
new_list = basket.count('a')  # it's a return method
print(basket)
print(new_list)  # it will return 2
