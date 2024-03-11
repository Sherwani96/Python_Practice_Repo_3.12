# super()

# there are two ways of inheriting the parent class attribute in child class
# 1. user.__init__(self, email), by calling the constructor of the parent class, we also need to pass this email attribute to child class constructor

class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power, email):  # implemented
        User.__init__(self, email)           # implemented
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with Arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50, 'abc@gmail.com')
archer1 = Archer('Robin', 500)
print(wizard1.email)

# 02. super().__init__(email)
# here we don't need to pass the self parameter to the parent class constructor, just difference here is we don't need to pass self
class User:
    def __init__(self, email):
        self.email = email

    def sign_in(self):
        print('Logged in')


class Wizard(User):
    def __init__(self, name, power, email):    # implemented
        super().__init__(email)                # implemented
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with Arrows: arrows left - {self.num_arrows}')

wizard1 = Wizard('Merlin', 50, 'abc@gmail.com')
archer1 = Archer('Robin', 500)
print(wizard1.email)
