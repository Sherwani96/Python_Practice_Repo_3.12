# OOP
# let's say we are working for a game development company
# we want to create a player class

class PlayerCharacter:
    def __init__(self, name):   # each param after self is an argument and we need to pass while instantiation
        self.name = name

    def run(self):           # here when we are inside the class we are making functions but inside it we call it a method.
        print('run')

player1 = PlayerCharacter('ali')    # using parentheses we are creating an object or instantiating
print(player1) # it will print <__main__.PlayerCharacter object at 0x000001B8A2C6D7C0> which is basically a memory location

# this dunder method __init__ is a constructor, this method is called every time when we instantiate. and is calling  to create an object
# when we are instantiating an object or using parentheses, we are calling the __init__ method which makes an object for us
# self refers to the PlayerCharacter here which is basically the class name
# self is a reference that hasn't been created yet, when the reference is created it will point to the object, which surely has some name in it that we pass as a parameter.
# so player1 is an object, which has a name 'ali'
# classes helps us to follow dry principle which is don't repeat yourself

class PlayerCharacter:
    def __init__(self, name, age):
        self.name = name            # attributes
        self.age = age              # attributes

    def run(self):
        print('run')

# an object can have attributes or properties
player2 = PlayerCharacter('Ahmed', 25)
player3 = PlayerCharacter('Ali', 30)

print(player2.age)  # here we are accessing the property of the object
print(player3.age)  # here we are accessing the property of the object

# we can also add attribute to a specific object
player2.attack = 50  # now attribute is defined or assigned to the object player2

print(player2.attack)
# print(player3.attack) # AttributeError: 'PlayerCharacter' object has no attribute 'attack'
