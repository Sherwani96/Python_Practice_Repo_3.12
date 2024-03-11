# list unpacking

# this phenomenon is called list unpacking
a,b,c, *rest = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)     # only 1 is assigned to variable a
print(b)     # only 2 is assigned to variable b
print(c)     # only 3 is assigned to variable c
print(rest)  # while here the rest of the list is assigned to variable rest

# another example
a,b,c, *rest, d = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a)     # only 1 is assigned to variable a
print(b)     # only 2 is assigned to variable b
print(c)     # only 3 is assigned to variable c
print(rest)  # while here the rest of the list is assigned to variable rest
print(d)     # only 9 is assigned to variable d
