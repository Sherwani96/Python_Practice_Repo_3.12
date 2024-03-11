# Scope - what variables do i have access to?

a = 1

def confusion():
    a = 5
    return a

print(a)
print(confusion())

# rules for scope in python (which interpreter checks for):

# 01 - start with local scope (inside the function)
# define: if there is no variable in local scope (function) it will check in global scope

a = 1 # global scope, now this value will be passed to this function
def confusion():
    return a

# 02 - parent local?
# define: if there is no variable in local scope (function) it will check in parent local scope(function)

a = 1 # global scope

def parent():
    a = 10
    def confusion():
        return a
    return confusion()

print(parent())
print(a)

# 03 - Global scope?
# if there is no variable exists in both parent and local scope it will check in global scope

a = 1 # global scope
def parent():
    def confusion():
        return a
    return confusion()

print(parent())
print(a)

# 04 - built-in python functions
# lastly if none of the above rules are true to the condition or met it will check in built-in python functions
# but this case will be only implemented for functions otherwise it will not work or give error

a = 1 # global scope
def parent():
    def confusion():
        return sum     # it will print <built-in function sum>
    return confusion()

print(parent())
print(a)