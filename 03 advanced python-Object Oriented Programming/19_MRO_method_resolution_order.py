# MRO - Method Resolution Order
# when you have such a complicated inheritance structure, you can use this method to find the order of the inheritence
# it follows d, b, c, a.
#  mro follows whats first in line, if things are common between classes

# class A:
#     num = 10

# class B(A):
#     pass

# class C(A):
#     num = 1

# class D(B, C):
#     pass

# print(D.mro()) # it prints the order or mro for this class D

class X:
    pass

class Y:
    pass

class Z:
    pass

class A(X, Y):
    pass

class B(Y, Z):
    pass

class M(B, A, Z):   # the mro order follows the sequence of the parameters we passed here
    pass

print(M.mro())
# alternate way
print(M.__mro__)

# algorithm for mro is depth first search
