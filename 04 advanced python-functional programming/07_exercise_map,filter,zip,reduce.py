from functools import reduce

#1 Capitalize all of the pet names and print the list
my_pets = ['sisi', 'bibi', 'titi', 'carla']

def capitalize(string):
    return string.upper()


new_list = list(map(capitalize,my_pets))
print(new_list)

#2 Zip the 2 lists into a list of tuples, but sort the numbers from lowest to highest.
my_strings = ['a', 'b', 'c', 'd', 'e']
my_numbers = [5,4,3,2,1]

def zip_list(strings,numbers):
    return list(zip(strings,numbers))

zipped_list = zip_list(my_strings, sorted(my_numbers))
print(zipped_list)

#3 Filter the scores that pass over 50%
scores = [73, 20, 65, 19, 76, 100, 88]

def passed_student(scores):
    return scores > 50

filtered_list = list(filter(passed_student, scores))
print(filtered_list)

#4 Combine all of the numbers that are in a list on this file using reduce (my_numbers and scores). What is the total?

my_numbers = [5,4,3,2,1]
scores = [73, 20, 65, 19, 76, 100, 88]

def accumulator(acc, item):
    return acc + item

total_list = reduce(accumulator,(scores, my_numbers))
print(total_list)