str, int  # here str, int or any other are builtin python functions

type_before = 100 #int
type_after = str(type_before) #now here it becomes string by calling within a builtin string function
type_previous = int(type_after) # now here it becomes integer again
print(type(type_before))
print(type(type_after))
print(type(type_previous))
