try:
    with open('./app/test.txt', mode='r') as my_file:
        print(my_file.read())
except FileNotFoundError as e:
    print('check your file path')