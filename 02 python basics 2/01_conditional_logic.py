# in this example consider driving license

is_old = False
is_licensed = False


# if is_old is set to False than if block is not going to execute, to execute it i need to add else block so this will execute
if is_old:
    print("You're old enough to drive")
elif is_licensed:
    print("You can drive now")
else:
    print("You're not old enough to drive")

# elif extends if block using another condition or logic
# if two blocks have same condition then it will execute first block
# when the condition is true and matched to first block or any then it will ignore the rest of the blocks and execute the first block
# when all conditions are false then it will execute the last block which is the else block
# there is only one if,else block while many elif blocks

is_old = True
is_licensed = False

if is_old and is_licensed:
    print("You're old enough to drive")
else:
    print("You're not old enough to drive")

# using and operator between two conditions
# if both conditions are true then it will execute the first block otherwise fall for the else block
