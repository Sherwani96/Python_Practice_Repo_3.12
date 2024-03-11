# oop
# polymorphism
# poly = many, morph = forms , which means many forms

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

# example # 01 of polymorphism
def player_attack(char):
    char.attack()

print(player_attack(wizard1)) # Attacking with the power of 50
# here attack method follows polymorphism, every player has their own attack method, but have attack tactics

for char in [wizard1, archer1]:  #here you can see both objects have attack method but have different attack tactics
    char.attack()

# --------------------------------------------------------------------------------------------

# having attack method in parent class and in child class
class User:
    def sign_in(self):
        print('Logged in')

    def attack(self):
        print('Do nothing')

class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        User.attack(self)              # user class attack method, because wanted to print simultaneously both parent and child class methods
        print(f'Attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with Arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50)
archer1 = Archer('Robin', 500)

print(player_attack(wizard1))