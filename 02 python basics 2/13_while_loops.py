# for loop For loop is used to iterate over a sequence of items. While loop is used to repeatedly execute a block of statements while a condition is true. For loops are designed for iterating over a sequence of items
# if you're using while loop you need to stop it otherwise it will run continuously and will crash the app

i=0
while i < 50:
    print(i)
    break        # it is used here to stop making it an infinite loop

# but now in below program i want to run the loop till 50 comes, now it will add one to i and will be changing it's value every time until 50
# we can also have else block in while loop
y=0
while y < 50:
    print(y)
    y += 1   # this is the same as y = y + 1, used short circuiting method
else:
    print('done all the work')

# else block use cases in while loop
# if i used break just below y += 1, then it wouldn't execute else block and print 'done all the work'
# when the while block condition turns to false then it will going to execute else block
# when break statement is used it will stop the entire loop means stop while loop and stop else block