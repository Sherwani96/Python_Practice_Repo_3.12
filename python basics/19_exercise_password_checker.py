# password checker

user_name = input('Please Enter Username: ')  #username
user_password = input("Please Enter your Password: ")  # password
hidden_password = len(user_password)
# to make the password secret or hid it we use asterisks
# trick we will be using her is print('*' * 10)


# we stored the msg in the variable
msg = f'{user_name}, your password {'*' * hidden_password} is {hidden_password} letters long'

print(msg)