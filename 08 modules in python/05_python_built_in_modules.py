import random
# built in modules in python, which might be called as standard library

# to access or check what this module offers, we use
# help(random)

# or we can use, dir to check how many methods it offers for this module
# print(dir(random))

print(random.random()) # this method generates a random number
print(random.randint(1,10))
print(random.choice([1,2,3,4,5]))
my_list = [1,2,3,4,5]
random.shuffle(my_list)
print(my_list)