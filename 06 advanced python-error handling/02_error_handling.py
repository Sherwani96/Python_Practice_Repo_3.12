# error handling

#  error handling allows us to let the script continue running
# try:
#     age = int(input('What\'s your age? '))
#     print(age)
# except:
#     print('Please enter an integer')

# in case if user didn't provide a valid input we don't want to stop the program, but definitely we want it to to run till it will get a valid input

# while True:
#     try:
#         age = int(input('What\'s your age? '))
#         print(age)
#     except:
#         print('Please enter an integer')
#     else:
#         print('Thankyou!!')
#         break

#  for multiple error types
while True:
    try:
        age = int(input('What\'s your age? '))
        print(10/age)
    except ValueError:
        print('Please enter an integer')
    except ZeroDivisionError:
        print('Please enter age higher than 0')
    else:
        print('Thankyou!!')
        break

# it will only check for one error type and comes back to the loop again