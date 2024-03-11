
# set comprehension example
my_set1 = {char for char in 'hello'}
print(my_set1)

my_set3 = {num*2 for num in range(31)}          # alternate
print(my_set3)

my_set4 = {num**2 for num in range(31) if num % 2 == 0}
print(my_set4)

# dict comprehension
simple_dict = {
    'a': 1,
    'b': 2,
}

my_dict = {k:v**2  for k,v in simple_dict.items() if v % 2 == 0}
print(my_dict)

# another example
my_dict2 = {num: num*2 for num in [1,2,3]}
print(my_dict2)