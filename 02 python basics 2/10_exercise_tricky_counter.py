# counter

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# the task here is to do addition of each items in the list

#declaring variable here what it does here it takes the value or item got from for loop and add it to the counter
# due to which variable changes or overrides each time when it takes out the value or item
counter = 0

for item in my_list:
    # counter = 0 , can also be declare here but what it will do here is that it will start from 0 each time
    counter = counter + item
    # what it does here it takes the value or item got from for loop and add it to the counter which is stored outside the for loop

print(counter)