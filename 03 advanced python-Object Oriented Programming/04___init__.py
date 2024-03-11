class PlayerCharacter:
    membership = True
    def __init__(self, name='Anonymous', age=0):  # defining value to the attributes in the constructor __init__ is called safeguard because it will helps you that right data type is provided or not
        if (age > 18):
            self.name = name
            self.age = age

    def shout(self):
        print(f'My name is {self.name}')

    def run(self, hello):
        print(f'My name is {self.name}, {hello} {self.name}')

player1 = PlayerCharacter('Ahmed', 18)  # it prints AttributeError: 'PlayerCharacter' object has no attribute 'name'
print(player1.shout())
# because we have provided the age is 10, the criteria for age is greater than 18 if not it will not call the __init__ constructor