# moving a file to a folder

with open('app/sad.txt', mode='r') as my_file:     # remember windows system follows \ backward slash for directory navigation
    print(my_file.read())
# it's a relative path

# for absolute path

with open('./app/sad.txt', mode='r') as my_file:
    print(my_file.read())

# we can use both file paths, here . means from the current folder
# here paths works according to the operating system, every os have different slashes or file paths
# an important module which is pathlib(object oriented file system path)
# pathlib takes care of the file path module for any system