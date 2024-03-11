
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
new_list = basket.sort()    # sort method alters the original list, it's a no return method
print(basket)
print(new_list) # it will return None as an answer
print(basket[::-1]) # it prints the list in reverse order

# reverse method
print("reverse method")
basket = ['a', 'x', 'b', 'c', 'd', 'e', 'd']
new_list = basket.sort()
new_list2 = basket.reverse()
print(basket)
print(new_list)
print(new_list2)

# range function
# The range function generates a sequence of numbers within a specified range.
# It can be used in a for loop or to create a list of numbers.
# it stops on 4 not on 5 because it follows (n-1)

# Example 1: Using range in a for loop
for num in range(5):
    print(num)

# Output:
# 0
# 1
# 2
# 3
# 4

# Example 2: Creating a list using range
                #start stop step
my_list = list(range(1, 10, 2))
print(my_list)

# Output:
# [1, 3, 5, 7, 9]

# Example 3: Using range with a step of -2
my_new_list = list(range(20, 1, -2))
# also this will print the list of even numbers from 20 to 1 in reverse order
print(my_new_list)

# Example 4: Using range with a step of -1
my_new_list = list(range(20, 1, -1))
# also this will print the list of odd numbers from 20 to 1 in reverse order
print(my_new_list)

# Example 5: Using range with a step of 1
my_new_list = list(range(1, 20, 2))
# also this will print the list of odd numbers from 1 to 20
print(my_new_list)

# Example 6: Using range with a step of 2
my_new_list = list(range(2, 20, 2))
# also this will print the list of even numbers from 1 to 20
print(my_new_list)

# .join() method
# it joins the elements of an iterable into one string
# it is used for strings only
# Example 1: Using .join() with a string
greet = ' '
new_greet = greet.join(['hello', 'there', 'how', 'are', 'you'])
# what it does here greet(which is a space string) joins new_greet in place of comma in between
print(greet)
print(new_greet)