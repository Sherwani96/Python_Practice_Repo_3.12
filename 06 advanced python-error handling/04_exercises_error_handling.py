# error handling

while True:
    try:
        age = int(input('What\'s your age? '))
        print(10/age)
    except ValueError:
        print('Please enter an integer')
        continue
    except ZeroDivisionError:
        print('Please enter age higher than 0')
        break
    else:
        print('Thankyou!!')
        break
    finally:
        print('ok, I\'m finally done')

# sequence of blocks execution details
# first it goes to try block it executed, then goes to except block none of the error occurs, an goes for else block and executes it
# after else block it get out of the loop and than does for finally block which it will definitely executes if there will be an error also
# normally finally block is used for logs to check on for user activity

