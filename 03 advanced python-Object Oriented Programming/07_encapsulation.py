# there are four pillars of OOP paradigm

# Encapsulation
# Inheritance
# Polymorphism
# Abstraction

# encapsulation = is the binding of data and the functions that manipulate that data
# and this data and functions are what we call attributes and methods

class PlayerCharacter:
    def __init__(self, name='Anonymous', age=0):
        if (age > 18):
            self.name = name
            self.age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self.name} and I am {self.age} years old')

player1 = PlayerCharacter('Ahmed', 25)
player1.speak()