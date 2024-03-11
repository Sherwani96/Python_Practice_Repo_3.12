
#   value/item    iterables
for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:
        print(item, x)

# iterables can be anything that has a collection of items
# list, tuple, set, dictionary, string
# iterated -> one by one check each item in the collection

user = {
    'name': 'ali',
    'age': 20,
    'city': 'karachi'
}

for item in user.items():
    print(item)

for item in user.keys():
    print(item)

for item in user.values():
    print(item)


# you can also name the items of iterable of your choice from iterables eg:
for k,v in user.items():
    print(k, v)