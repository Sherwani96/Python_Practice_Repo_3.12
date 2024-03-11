# we can also use with statement, if we don't want to use close statement

with open('test.txt', mode='w') as my_file:
    print(my_file.readlines())

# open also accepts another parameter which is mode, if we don't provide mode by default it takes read or r
# in order to read and write we use r+

with open('test.txt', mode='r+') as my_file:
    text = my_file.write('hey it\'s me')
    print(text)

# when we write something to a file the cursor resets
# if some text exists there it will be overwrite
# in order to prevent from over writing we use 'a' append mode

with open('test.txt', mode='a') as my_file:
    text = my_file.write(':)')
    print(text)

#  if i use write mode only it will create a new file if it doesn't exists
# write also over writes or replaces the content of a file