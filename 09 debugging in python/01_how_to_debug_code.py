# debugging

# to constantly improve your code you need to find more and more mistakes
# removing bugs or errors from our code is called debugging

# linting
# linting helps debug code before runtime
# ide's or code editors have code's standard formatting tools

# pdb = python debugger
# pdb is a builtin module in python
import pdb

def summed(num1,num2):
    pdb.set_trace()
    t = 3 + 4
    return print(num1 + num2)

summed(2, 'heeke')

# after finding bug you can remove pdb code line, it's just debug our code,  that everything is working fine
# you can check variable, to see it's value by only inserting the variable name which is t here
# typing help command will open the window for other commands which will be helpful , while it's only possible when used pdb in the code
# we can also change the variable value inside the pdb debugger environment