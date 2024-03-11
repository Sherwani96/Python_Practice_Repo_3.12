# @classmethod and @staticmethod are decorators

class PlayerCharactr:
    membership = True
    def __init__(self, name='Anonymous', age=0):
        if (age > 18):
            self.name = name
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    def run(self, hello):
        print(f'My name is {self.name}, {hello} {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return num1 + num2

# player1 = PlayerCharacter('Ahmed', 18)

# print(PlayerCharacter.adding_things(2,3)) # just like this we can use class method

# the reason here is that why we use class method instead of defining simple function which uses self
# we can use methods define inside classes without instantiating the class


class PlayerCharacter:
    membership = True
    def __init__(self, name='Anonymous', age=0):
        if (age > 18):
            self.name = name
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    def run(self, hello):
        print(f'My name is {self.name}, {hello} {self.name}')

    @classmethod
    def adding_things(cls, num1, num2):
        return cls('teddy', num1 + num2)                 # instead we use cls here to instantiate an object

    @staticmethod
    def adding_things(num1, num2):
        return  num1 + num2

player3 = PlayerCharacter.adding_things(2,3)

print(PlayerCharacter.adding_things)

# the only difference between the two methods is cls
# in class method we do care about class attributes defined in the constructor and we modify them