# truthy vs falsy

truthy_is_old = bool(34)  # here it's converted to true
truthy_is_licensed = bool('licensed') # here it's converted to true

falsy_is_old = bool(0)  # here it's converted to false
falsy_is_licensed = bool('') # here it's converted to false

if truthy_is_old and truthy_is_licensed:
    print("You're old enough to drive")
else:
    print("You're not old enough to drive")

# python interpreter takes the variable values as true or false
# it converts the value to true or false than it goes to if block or else block and execute it

