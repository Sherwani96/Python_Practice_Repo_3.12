# decorators
# it's simply a function that wraps another function and enhances it or change it

def my_decorator(func):
    def wrap_func():
        print('***********')
        func()
        print('***********')
    return wrap_func

# when we use @ before it says it's a declaration for python decorator function

@my_decorator     # this means that this is the top function
def hello():
    print('helloooo')

@my_decorator
def bye():
    print('see you later')

# hello()
bye()

# here hello function will passed to the wrapper function and will be called or invoke from there
