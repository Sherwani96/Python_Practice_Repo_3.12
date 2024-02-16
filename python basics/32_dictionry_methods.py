# dictionary

user = {
    'basket': [1, 2, 3],
    'greet': 'hello there!!'
}

# print(user['age']) # it will throw an error because age is not exists in the dictionary

# remember errors in programs are not good. we need to handle them
# if we don't handle the error it will crash the program
# we can handle the error by using try and except which we will do in later topics.

# for the time being we will just handle the error using dictionary's get method
user = {
    'basket': [1, 2, 3],
    'greet': 'hello there!!'
}
print(user.get('age')) # it will return None but not error

# another way of using get method is accessing the value of a key if it doesn't exists
user = {
    'basket': [1, 2, 3],
    'greet': 'hello there!!'
}
print(user.get('key=age', 'the value of age')) # what it says here if key doesn't exists than return it's value which is 'the value of age'
# but what if the value is defined or the key exists so it will return the previously defined value

# another of declaring dictionary is
user_2 = dict(name = 'ahmed', age = 27) # here dict is a function
# remember key here is passed as a variable or kwargs so it shouldn't be enclosed in quotation

# usually it's not a common way to declare dictionary.
print("in method")
user = {
    'basket': [1, 2, 3],
    'greet': 'hello there!!'
}
# 1st way of checking item in dictionary
print(1 in user['basket']) # it tells True here

# 2nd way of checking item in dictionary
print(user.keys())
# this will provide all exits that exists in dictionary

# if i don't want to check all the keys but rather just check one, so
print('greet' in user.keys()) # it tells True here

# just like keys method there is also a method for accessing values
user = {
    'basket': [1, 2, 3],
    'greet': 'hello there!!'
}
# both ways can be used to check values
print(2 in user.values()) # it tells false here because it is inside list to do this we need to use 2nd option below
print(2 in user['basket']) # it tells True here
print(user.values()) # it will return all values in dictionary

# items method
user = {
    'basket': [1, 2, 3],
    'greet': 'hello there!!'
}
print(user.items())
# it returns items of dictionary as list of tuples

# clear method
user = {
    'basket': [1, 2, 3],
    'greet': 'hello there!!'
}
user.clear()
print(user) # it will return empty dictionary

# copy method
user = {
    'basket': [1, 2, 3],
    'greet': 'hello there!!'
}
user2 = user.copy()
user.clear()
print(user2)
print(user)

# using copy method if you ake alterations it wouldn't change the original dictionary or the copy dictionary

# pop method
user = {
    'basket': [1, 2, 3],
    'greet': 'hello there!!',
    'age': 27
}
user2 = user.pop('age')  # here pop is a return method
print(user)              # pop(key) method takes argument or key 
print(user2)             # result is only the value of the key that is passed as an argument

# popitem method
user = {
    'basket': [1, 2, 3],
    'greet': 'hello there!!',
    'age': 27
}
user2 = user.popitem()  # here pop is a return method and it only pops or removes the key not the value
print(user)             # popitem() method doesn't take any argument
print(user2)            # result is the key and value as a tuple of the last item that is popped or removed

# update method
user = {
    'basket': [1, 2, 3],
    'greet': 'hello there!!',
    'age': 27
}
user.update({'age': 40}) # it will update the age
user.update({'ages': 20}) # it will add new key and value
print(user)
