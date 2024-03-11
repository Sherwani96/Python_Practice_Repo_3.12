# instance

class User:
    def sign_in(self):
        print('Logged in')

class Wizard(User):    # passing user class to inherit from parent
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with the power of {self.power}')

class Archer(User):    # passing user class to inherit from parent
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with Arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 500)

# isinstance method, is used check if an object is an instance of a class
print(isinstance(wizard1, Wizard)) # True
print(isinstance(wizard1, User)) # True
print(isinstance(wizard1, object)) # True

# everything in python is an object and every object inherits from python base class which is object