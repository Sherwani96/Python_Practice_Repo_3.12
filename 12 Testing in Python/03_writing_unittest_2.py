# python -m unittest
# above will run all the test cases you'll have

# python -m unittest -v
# v for verbose
# above command will provide the result separately for each unittest

# we can also use doc string but it must on same line or one line
# using python -m unittest -v, will print the status of testcase along with docstring

# we can use a function to print something while checking or running for each testcase
# python -m unittest -v, setup for above is just define function like this below the testcase class
# def setUp(self):
#     print("about to test a function")

# we also use a function to clear some variable, and is defined at the bottom of the class
def tearDown(self):
    print('cleaning up')