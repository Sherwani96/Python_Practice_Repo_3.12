# oop

# inheritance
# inheritance = is a process in which one class acquires all the properties of another class
# inheritance allows new objects to take on the properties of existing objects, so you can inherit classes

# let's consider an example we want to create a new game which has many users
# some users or players have common functionality but have different attack tactics
#  children classes are sometimes called subclasses or derived classes

# user = wizard, archer, ogres
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

print(wizard1.sign_in())
# print(archer1.sign_in()