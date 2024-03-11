import re
# regular expressions are used when validation is required like email, or password

string = 'search inside of this text please!!'

# print('search' in string) # this is the alternate way
val = re.search('of', string)  # <re.Match object; span=(14, 16), match='of'>
# this prints the index no of that particular object we have provided
print(val.span()) # span will print the index no. of the string

print(val.start()) # start tells us that when the string starts to occur

print(val.end()) # end tells us that when the string ends

print(val.group())  # it prints that string, if repeated more than once it will print once only
# group is useful when we ty to do multiple searches

# incase if it finds nothing it will return none, also shows the error

# we can also do like this
string = 'search this inside of this text please!!'
pattern = re.compile('inside of this')  # here we assign the pattern or keyword we are searching for, we don't need to use re for the rest variables
a = pattern.search(string)
b = pattern.findall(string)   # this will print all the instances or occurrences
c = pattern.fullmatch(string)  #this will only print if the string we're looking for and the saved string both are same, otherwise it will print none
d = pattern.match(string) # it prints that the passed string is matching the stored string, it doesn't care like fullmatch method
print(d)

