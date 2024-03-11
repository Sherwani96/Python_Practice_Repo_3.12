# functions jst act like variables

def hello():
    print('hellllooooooooo!')

greet = hello()
del hello
# print(hello)
print(greet) # while it can be called just using variable
# print(greet()) # while here it cannot be called as a function here
# here using python del keyword to delete hello() function, hello functions is stored as an object to some location in memory
# while hello function is deleted but at the same time hello() was assigned to greet, it stored that function but was deleted from memory

# calling function into another function
def hello(func):
    func()

def greet():
    print('hello there')

greet_msg = hello(greet)
print(greet_msg)

# decorators super charge our functions
