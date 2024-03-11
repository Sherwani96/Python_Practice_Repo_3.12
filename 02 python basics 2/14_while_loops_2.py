# it's totally upto where do you want to use for or while loop

# using for loop
my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)


i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1

# another use case of while loop
while True:
    input('Enter something: ')
    break
# what break statement does here it breaks the loop, if i didn't break the loop it will keep running/asking same question in cli

# but another trick to stop while loop is continuing the above example
while True:
    response = input('Enter something: ')
    if response == 'bye':
        break

# using if loop here helps to meet the condition if it is met then it will break the loop otherwise it will ask repeatedly
