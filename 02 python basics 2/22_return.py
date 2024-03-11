# return is used in functions

def sum(num1, num2):
    num1 + num2 # it prints None, because it's not returning anything

print(sum(3,4))

# to solve this we need to use return keyword before the expression we want to return
def sum(num1, num2):
    return num1 + num2 # it prints 7

print(sum(3,4))

# function should return something
def sum(num1, num2):
    print('hello')
    num1 + num2 # it prints 7

print(sum(3,4))

# return helps us to store the value in a variable
# now we are going to store the value of a function in a variable
def sum(num1, num2):
    return num1 + num2

value = sum(2,5) # here sum function is calling or invoking
print(value) # it prints 7
value2 = sum(3,value)
print(value2) # it prints 10

# functions can be nested
def sum(num1, num2):
    def another_func(num1, num2):     #here the params are num1 and num2
        return num1 + num2           # here it returns the sum of num1 and num2
    return another_func(num1, num2)  # here it returns the sum of num1 and num2 which were passed to another_func
# here sum function is returning another_func function which is returning the sum of num1 and num2
# while function does nothing it is returning the whole body of the function another_func

print('new function')
def sum(num1, num2):
    def another_func(n1, n2):
        return n1 + n2
    return another_func(num1, num2)

total = sum(10, 22)
print(total)

print('----------------------')

def check(n1, n2):
    def check2(n3, n4):
        return n3 + n4
    return check2(n1, n2)

val = check(11,56)
print(val)

# what we are doing here we are returning another function and passing the params of pre defined function to another function
print('----------------------------')
def body(fname, emoji):
    def greet(name, emoji):
        return print(f'Hello {name} {emoji}')
    return greet(fname, emoji)

greeting = body('Ali', '😊')
print(greeting)