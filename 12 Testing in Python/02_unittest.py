
# main file code
def do_stuff(num):
    return num + 5

# test file code
import unittest
import main

class TestMain(unittest.TestCase):    # here we are inheriting whatever unittest testcase is
    def test_do_stuff(self):               # here we are passing function as a method
        test_param = 10
        result  = main.do_stuff(test_param)  # here we are saying that go to main module check for that function and pass the param
        self.assertEqual(result, 15)   # here the param(result) is the calculated amount by the interpreter and 15 is the actual answer. if both same test will be pass



# another unit test case which only checks for the value if it is true or not
    def test_do_stuff2(self):
        test_param = 'abcdef'
        result  = main.do_stuff(test_param)
        self.assertTrue(result, ValueError)


#  using isinstance method
    def test_do_stuff3(self):
            test_param = 'accvd'
            result  = main.do_stuff(test_param)
            self.assertIsInstance(result, ValueError)

# test for providing param of none type, this is the the case only followed when you will either provide None type or provide nothing
    def test_do_stuff4(self):
            test_param = None
            result  = main.do_stuff(test_param)
            self.assertEqual(result, "Please enter number")

    def test_do_stuff5(self):
            test_param = ''
            result  = main.do_stuff(test_param)
            self.assertEqual(result, "Please enter number")

unittest.main()     # this will run the test for the main file
