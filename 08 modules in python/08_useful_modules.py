from collections import Counter, defaultdict, OrderedDict

li = [1,2,3,4,5,6,7,7]
sentence = 'blah blah blah thinking about python'
# print(Counter(li))  # it will count the no of occurrence of each item
print(Counter(sentence)) # it will count no of occurrence of each letter

dictionary = defaultdict(lambda: 'doesn\'t exists', {'a': 1, 'b': 2})  # by default defaultdict accepts callable function before
print(dictionary['c'])  # it prints 5 here if the value for the key doesn't exists


# -----------------------------------------------------------------
# simple dictionary
dict1 = {'a': 10}
dict1['b'] = 20
dict1['c'] = 30

dict2 = {'a': 10}
dict2['c'] = 30
dict2['b'] = 20

# if we compare both dictionaries, it will return true because dictionaries are unordered
print(dict1 == dict2) # it prints true

# while using collection's orderedDict method, we will be using ordered dictionary
dict3 = OrderedDict({'a': 10})
dict3['b'] = 20
dict3['c'] = 30

dict4 = OrderedDict({'a': 10})
dict4['c'] = 30
dict4['b'] = 20

print(dict3 == dict4) # it prints false
