# sometimes errors and exceptions can be so severe that we don't want to stop our programs from running
# we do want to catch them with the except block, but at the same time also stop whatever the program is doing


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

# to make your own errors we use {raise errortype("msg")}
# we can slo use exception {raise exception('msg')}