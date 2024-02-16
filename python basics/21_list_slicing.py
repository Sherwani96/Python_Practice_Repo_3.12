# list slicing

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

print(amazon_cart) # it will print the whole list

# Now moving towards the list slicing
print(amazon_cart[1::2]) # it will print the list from index 1 till the end with step of 2
print(amazon_cart[::2]) # it will print the list from index 0 till the end with step of 2
print(amazon_cart[0:2]) # it will print the list from index 0 till index 1

# moving towards the mutable list
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]
# in the above shopping cart i want to add laptop so making it a third priority in the list
# what will do here it will just swap or replace the toys with laptop
amazon_cart[2] = 'laptop'
print(amazon_cart)

# copying or assigning same list to a new variable
amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

new_cart = amazon_cart
new_cart[0] = 'watch'
print(amazon_cart)
print(new_cart)

# when assigning amazon_cart to new_cart and what does amazon_cart equals to amazon_cart points somewhere in the memory which says here is the amazon_cart
# instead of copying it will just point to the same location of amazon_cart in the memory

# what if we want to copy the list without changing the original list so what we do here is

amazon_cart = [
    'notebooks',
    'sunglasses',
    'toys',
    'grapes'
]

new_cart = amazon_cart[:]  # using slicing we can copy the list
# now it won't update the content of amazon_cart it's a copy now
new_cart[0] = 'watch'
print(amazon_cart)
print(new_cart)
