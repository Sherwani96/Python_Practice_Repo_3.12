# list comprehensions are also called set comprehensions or dictionary comprehensions

# body = [param for param in iterable]

# list comprehension example
my_list1 = [char for char in 'hello']
print(my_list1)

# numbers list
num_list2 = [num for num in (map(lambda x: x*2, range(20)))]  # alternate
print(num_list2)

num_list3 = [num*2 for num in range(31)]          # alternate
print(num_list3)

# exponential with even values
my_list4 = [num**2 for num in range(31) if num % 2 == 0]   # using for loop and if together in list comprehension
print(my_list4)

# for better code understanding while using list comprehension is using comments to help others to understand
