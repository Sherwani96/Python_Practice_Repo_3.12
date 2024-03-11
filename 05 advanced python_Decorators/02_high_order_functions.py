# higher order function hoc
# there are two types of hoc function
# one who takes function as a param
# second who returns function

def greet(func):   # here greet is high order function, while it takes function as a param
    func()

def greet2():
    def func():
        return 5
    return func

# map, reduce and filter are higher order functions