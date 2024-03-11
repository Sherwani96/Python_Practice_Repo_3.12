from random import randint
import sys
# generate a number 1 to 10

generated_num = randint(int(sys.argv[1]), int(sys.argv[2]))

# input from user

while True:
    try:
        user_value = int(input('Please choose a number between those two you just chose: '))
        if user_value >= int(sys.argv[1]) and user_value <= int(sys.argv[2]):
            if user_value == generated_num:
                print('You\'re genius, You won the Game!!')
                break
    except ValueError as err:
        print('Please enter a number')
        continue