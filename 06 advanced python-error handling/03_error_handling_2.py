# error handling
# for descriptive error message we use err along with error type and also in print statement
# we can also use multiple error types with same message like (TypeError, ZeroDivisionError), now the print msg will be shown to both error types
# except (TypeError, ZeroDivisionError) as err:
#  can also use like above



def sum(num1, num2):
    try:
        return num1 + num2
    except TypeError as err:
        print('Please enter numbers ', err)


print(sum(1, '2'))
