# "docstrings" in python are used to document the code

def test(a):
    '''
    Info: this function is used to test docstring which accepts param a
    '''
    print(a)

test('hello')

# docstrings are used to add function docs or describes about function that what it will going to do
# how do we know that how it works?
# while calling or invoking function hover on the function name and it will show the docstring

# to know about any function that why and how it is used?
# we can use help function
help(test) # it will show the docstring

# another way is using the __doc__ attribute or the dunder method
print(test.__doc__) # it will show the docstring
