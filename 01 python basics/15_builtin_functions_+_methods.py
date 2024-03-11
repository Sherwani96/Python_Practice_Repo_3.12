
print(len('hello')) # here the total length of the string object is 5
print(len('hello world')) # here the total length of the string object is 11 because it also counts space character.

# we can also use len function in slicing
greet = "hello ahmed"
print(greet[2:len(greet)]) # what it does here it starts counting from 2nd index till length of greet object.

# methods in python are accessible by using .any_method like

value = 'hello there!!'
new_value = value.upper() # here .upper is a string method just right after it we are calling it
print(new_value)

msg = 'to be or not to be'
print(msg.replace('be', 'me')) 

# remember note one thing here strings are immutable through index method using [], while editable using 
# .replace() string method

# if we recall the edited msg variable it'll show the od one not he updated one because we used .replace method without assigning to any variable so that's why it's not updated
# if need to update it we need to assign it to new variable otherwise it'll be lost because print function is non return function.


