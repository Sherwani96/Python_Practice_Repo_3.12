
print(True == 1)   # it will print True
print('' == 1)     # it will print False
print([] == 1)     # it will print False
print(10 == 10.0)  # it will print True
print([] == [])    # it will print True

# what == checks above is equality or equality of value
# empty string or list or any other object which is empty is basically falsy means False, false in binary is 0
print('1' == 1) # it will print False

# is check the memory location of both comparing objects
print('checking is operator')
print(True is True) # it will print True
print('1' is '1')     # it will print True
print([] is [])     # it will print False
print(10 is 10)     # it will print True
print([1,2,3] is [1,2,3]) # it will print False

# every same data structure with dame values have different memory location and will print False if using is operator, while true if using ==
# every same data types have same memory location will print True if using is operator
