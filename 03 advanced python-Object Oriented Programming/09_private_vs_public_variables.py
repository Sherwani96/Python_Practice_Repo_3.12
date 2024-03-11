# private variables vs public variables

# in python there is no privacy, there is no true private variables
# if there is _ before variable, it's just a convention, as a python programmer, if we see any underscore in the variable name, it's private
# we just use _ just to tell other programmers that pls don't touch this variable
# this way privacy is achieved in python by using _ in front of the variable name
# using _ in front of the variable name will make it private
# using __ in front of the variable name will make it protected

class PlayerCharacter:
    def __init__(self, name='Anonymous', age=0):
        if (age > 18):
            self._name = name
            self._age = age

    def run(self):
        print('run')

    def speak(self):
        print(f'My name is {self._name} and I am {self._age} years old')

player1 = PlayerCharacter('Ahmed', 25)
print(player1.speak())


# dunder methods
# we cannot write our own or override dunder methods because it's not a good practice
