#  Scope - what variables do i have access to?
# scope - where do i have access to variables
#  scope exists in other programming languages also

x = 10000
def checking_scope():
    total = 100   # variables defined in scope are limited to that function only
    print(total)  # while here it can access the variable
    print(x)
checking_scope()
# print(total) # here it cannot read variable 'total' or can't access it.
# also we can access the variable 'x' inside the function

# using if loop for defining scope
if True:
    total = 100

print(total) # here we can access the variable 'total' and can print it

# so for functions variable is limited to that function only