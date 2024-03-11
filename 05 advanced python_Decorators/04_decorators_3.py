# decorator pattern

def my_decorator(func):
    def wrap_func(x):
        print('***********')
        func(x)
        print('***********')
    return wrap_func

@my_decorator
def hello(greet):
    print(greet)

# hello("hello there!!!!")

greet_func =  hello('Hey you how are you!!!!')

print('# -------------------------------------------------------------')

# having two params

def my_decorator(func):
    def wrap_func(*args, **kwargs):
        print('***********')
        func(*args, **kwargs)
        print('***********')
    return wrap_func

@my_decorator
def hello(greet, emoji= '😀'):
    print(greet, emoji)

func_with_emoji = hello(f'Hi {input('what\'s your name?:')}!!!, Hope you are fine')