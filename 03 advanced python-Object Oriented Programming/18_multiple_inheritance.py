class User:
    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def check_arrows(self):
        print(f'Attacking with Arrows: arrows left - {self.num_arrows}')

    def run(self):
        print('Ran faster')

class HybridBorg(Archer, Wizard):       # we can pass as many parameters as we can
    def __init__(self, name, power, num_arrows):
        Archer.__init__(self, name, num_arrows)
        Wizard.__init__(self, name, power)


hb1 = HybridBorg('Haris', 50, 3)
print(hb1.num_arrows)
print(hb1.sign_in())

# Multiple Inheritance is not allowed in some of the programming languages