# clean code

def is_even_or_odd(num):
    '''
    Info: This functions is used to check if a number is even or odd
    '''
    if num % 2 == 0:
        return 'Even Number'
    else:
        return 'Odd Number'

print(is_even_or_odd(3))

# another way of writing above code
def is_even_or_odd(num):
    if num % 2 == 0:
        return True
    return False

print(is_even_or_odd(3))

# clean code

def is_even(val):
    return val % 2 == 0

print(is_even(1))