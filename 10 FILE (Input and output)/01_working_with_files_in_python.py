# we can input an image and give output as a compressed image

# python has builtin function 'open' which allows us to open and write files

my_file = open('test.txt')
print(my_file.read())
print(my_file.read())
print(my_file.read())

# we can read the file once or print it once because it follows where cursor is
# it will print but only empty spaces, means two empty lines
# you just wrote a print command, the command is being read from the start and moved the cursor to the end after reading, and it sees nothing after that

# in order to prevent from the cursor behavior we use
print(my_file.read())
my_file.seek(0) # it brings the cursor to the beginning of the next line
print(my_file.read())
my_file.seek(0)
print(my_file.read())

#  the alternate way is using readline
print(my_file.readline())

# this will return entire content in a list using readlines
print(my_file.readlines())

# note: remember when w e open th file using open(), we must hav to close it, as it is a standard procedure
my_file.close()  # that's it
