# type conversion

name = 'Ahmed'
age = 27
relationship_status = 'single'

# now here i want to change my relationship status
relationship_status = 'It\'s complicated\n' # here it's updated or reassigned
print(relationship_status)


# here is the program which guess your age
birth_year = input('In which year you\'re born?')

if (birth_year):
    age = 2024 - int(birth_year)    # here i need to change the type because the value we get through input function is by default string in type
    print(f"You are {age} year's old")
else:
    print("Please Enter your Birth Year")