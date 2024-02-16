# dictionaries are used to store key value pairs
# in other programming languages like javascript it is called an object, while in python it is called a dictionary
# dictionaries are mutable
# dictionary is always enclosed in curly braces {}
# in dictionary we can store any type of data

dictionary = {
    'a': [1 , 3, 'red'],
    'b': True,
    'c': ('error', 'warning', 'info', 34),
    'x': 'hello',
    'y': 34
}

dictionary['y'] = 49 # adding new key value pair

print(dictionary) # this will print the entire dictionary
print(type(dictionary))  # this will print the type of dictionary which is dict
print(dictionary['a']) # this will print the value of key 'a'
print(dictionary['x']) # this will print the value of key 'x'

# an array can have a list of dictionaries

my_list = [
    {   'name': 'ahmed',
        'id': 2,
    },
    {
        'name': 'ali',
        'id': 34
    }
]

print(my_list)

another_list = [
   {'1': 'ali', '2': 'ahmed'},
   {'1': 'iftikhar', '2': 'saqib'},
]
print(another_list)
print(another_list[0]['1']) # it prints ali here