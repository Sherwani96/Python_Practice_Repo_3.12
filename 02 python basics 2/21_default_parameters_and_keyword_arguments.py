# positional arguments are arguments that are need to be placed in specific order or position.


def say_hello(name, emoji):
    print(f'Hello {name} {emoji}')


# positional arguments
say_hello('Ahmed', '😊')

# in keyword arguments position doesn't matter
say_hello(emoji = '😊', name = 'Ahmed')
# you can use keyword arguments but it's little bit confusing for other programmers who read your code
# using keyword arguments making the code difficult
# keyword arguments are also called as kwargs
# if you are using kwargs using

# default parameters
def say_hello(name = 'John Doe', emoji = '😊'):
    print(f'Hello {name} {emoji}')

say_hello()

# where do we use default parameters
# we usually use functions with default parameters wither if we want or forget to pass arguments while calling function
# (continue) what it will do it will use the same parameters which were passed during defining function
#  or we are setting it's default value
# we can manipulate it by passing new arguments while calling function
