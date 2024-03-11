# OOP
# oops helps to write code that is repeatable, well organized and also memory efficient because we only write this once
# in vs code intellisense purple box is method

# using help we can access the blueprint
# help(list)

# attributes are pieces of data that are dynamic

# class PlayerCharacter:
#     # Class object attribute, it's not dynamic it's static, it's going to be same for all the objects
#     membership = True
#     def __init__(self, name, age):
#         self.name = name            # attributes
#         self.age = age              # attributes

#     def run(self):
#         print('run')

# here we are going to check if membership exists then allow constructor for instantiation
class PlayerCharacter:
    # Class object attribute, it's not dynamic it's static, it's going to be same for all the objects
    membership = True
    def __init__(self, name, age):
        if (self.membership):        # we can also use PlayerCharacter.membership instead of self.membership
            self.name = name            # attributes
            self.age = age              # attributes

    def shout(self):
        print(f'My name is {self.name}') # here we cannot pass PlayerCharacter.membership because it is not an attribute of PlayerCharacter it is passed or used inside a constructor

    def run(self, hello):
        print(f'My name is {self.name}, {hello} {self.name}')

# anything that is defined or declared inside a constructor we need to access it through self.attribute
player1 = PlayerCharacter('Ahmed', 25)
player2 = PlayerCharacter('Ali', 30)

print(player1.run('hello!!!!!'))
print(player2.shout())
