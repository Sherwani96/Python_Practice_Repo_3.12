# logical operators

# 01 greater than
print(5 > 4) # it will print True
# here ASCII value of 'a' is 97 and ASCII value of 'b' is 98
print('a' > 'b') # it will print False
# here value of 'a' is 97 nad 'A' is 65 because interpreter converts characters to ASCII code or values than compares it
print('a' > 'A') # it will print True


# 02 less than
print(5 < 4) # it will print False
print('a' < 'b') # it will print True, because it compares values in ASCII code values so that it will print True
print('a' < 'A') # it will print False
# In alphabets order the letter comes after or the successor will always be greater than predecessor

# 03 double equals ==
print(5 == 4) # it will print False
print('hi' == 'hello') # it will print False

# 04 equals to =
# print(5 = 4) # it will give error because it is an assignment operator not a logical operator
# it is used to assign values to the variables

# 05 greater than and equals to >=
print(2 >= 1) # it will print True

#06 less than or equals to <=
print(2 <= 1) # it will print False

# 07 not equals to !=
print(2 != 1) # it will print True
# it is basically opposite to ==
# it will print true for rest of the numbers but not for 1, for 1 it will print false
# what it defines for 1 is not equal to 1

# not operator gives the opposite value
print(not True) # it will print False
print(not False) # it will print True