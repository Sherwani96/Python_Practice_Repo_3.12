# walrus operator is represented by := syntax
# walrus operator assigns value to the variable

# example # 01
greet = 'hello there!!!'

if ((n := len(greet)) > 5):
    print(f'{greet} is {n} characters long')

# example # 02 of walrus operator using while it takes out every letter each time until it met the condition
greet = 'hello there!!!'
while (n := len(greet) > 1):
    print(n)
    greet = greet[:-1]

# example # 03
numbers = [1, 2, 3, 4, 5]
while (n := len(numbers) > 0):
    print(numbers.pop())

# example # 04
greet = ['hello there!!!']
while (n := len(greet) > 0):
    print(greet.pop())

print(greet)

# example # 05
sample_data = [
    {"userId": 1,  "name": "ahmed", "completed": False},
    {"userId": 2, "name": "ali", "completed": False},
    {"userId": 3,  "name": "hamza", "completed": False},
    {"userId": 4,  "name": "khalid", "completed": True}
]

for entry in sample_data:
    if name := entry.get('name'):
        if name:
            print(f'Found name: {name}')

# example # 06
foods = list()
while (food := input('what food do you like? ')) != 'quit':
    foods.append(food)

# __________ another approach below ______________

# example # 07
print('ss')
foods = list()
while True:
    food = input('what food do you like? ')
    if food == 'quit':
        break
    foods.append(food)

