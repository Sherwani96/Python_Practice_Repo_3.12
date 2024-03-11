# strings in python are immutable. here immutable means cannot be changed or editable after assigned to the variable.

# eg
# while assigning
value = '123456'
# after assigning it is immutable. we cannot change the value later on.
value[0] = '9'
# while reassigning
value = '0123' # now the value is changed
print(value)
# it shows the below error
# TypeError: 'str' object does not support item assignment
# but we can change the value only by reassigning it to the variable
