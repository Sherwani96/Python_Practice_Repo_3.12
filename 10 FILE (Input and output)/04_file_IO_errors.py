# another common way or best practice for working with files is using try except block

try:
    with open('./app/sad.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as err:
    print('File does\'nt exists')
    raise err
except IOError as err:
    print('IO error')
    raise err


# io error is one which occurs by os during reading or writing a file
