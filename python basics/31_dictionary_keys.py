dictionary = {
    123: [1,2,3],
    True: 'hello',
    (23, 'hi'): "Tuple"  # it can pass tuple as a key because it is immutable data structure
    [100]: 33         # TypeError: unhashable type: 'list', while list is mutable
}
# list cannot be assigned as a key because it is a data structure type while 123 and True are data types
# so it can accept only immutable data structures or data types that cannot be changed or editable
# because it only accepts keys which are immutable
print(dictionary)

same_key = {
    '123': [1,1,2,3,4],
    '123': 'Hello!!'     # here same key with different values are assigned
}
# but what it actually does here it'll going to override the previous key with the new one
# it will print the last key value pair which is 'Hello!!'
print(same_key)

# so the best practice is to use unique keys