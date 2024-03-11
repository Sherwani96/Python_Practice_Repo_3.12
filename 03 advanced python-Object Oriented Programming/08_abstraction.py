# oop

# Abstraction

# abstraction = is the process of hiding unwanted data and showing only essential data
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
player1.speak = 'hello' # because of overriding the speak method, it prints TypeError: 'str' object is not callable, print(player1.speak()), so we use print(player1.speak) because it's not a method anymore
print(player1.speak)

# here speak method is implementing abstraction as we don't want to see how it works or how many methods does this instantiated object have
# or in simplified words we just use methods to act without focusing on how it works in the background
# same goes for functions or builtin python functions too  print(len(1,2,3,4))
