# break, continue, pass
# we can also use break, continue, pass statements
# when we use break statement it breaks the loop and get out of it
# using continue statement, it brings the interpreter to the very first line of the loop and continues iteration
# passing statement is used to do nothing in the loop, it just passes to the next line
# just like you write any loop and want to skip the error of not having a code block in the loop, you can use pass statement
# for pass statement you're thinking about the logic and wnt to run the rest of the code so you can use pass instead
# it skips the error and just runs the rest of the code

my_list = [1, 2, 3, 4, 5]

for item in my_list:
    print(item)
    continue

i = 0
while i < len(my_list):
    print(my_list[i])
    i += 1
    continue