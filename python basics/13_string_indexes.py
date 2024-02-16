# string indexes

word = 'be hi ky'
      # 01234567

# every single letter or even special character or space between are stored in different locations of memory.
# by using string we can access different parts/elements of string.
print(word[0])
print(word[1])
print(word[2])
print(word[3])
print(word[4])
print(word[5])
print(word[6])
print(word[7])
print("using index method to access desired element or indexes within string")
# remember one thing that it will not print the exactly mentioned stop point in string's index what exactly it will do it subtracts -1 (n-1)
# word[start:stop] start point is 0 while it stopped on 3 not 4 because it follows (n-1)
print(word[0:4])

# word[start:stop:stepover] it uses jump over and skip the sequence when mentioned
# here it is called string slicing
print(word[0:8:2]) # what it does here in it "be hi ky" it jumps from b to the space character than on i and k ans is "b ik"

numbers = '23456789'
print(numbers[1:]) # what it will do here it will print the sequence from 1st index till end ans is(3456789)
print(numbers[:5]) # what it gonna do it will print till the 5th index ans is (23456)
print(numbers[::2]) # what it does here jumping over ever 2 steps ans is (2468)
# although it's upto you whether what jumping sequence you want or whether you don't. but if when you don't want it so don't mention it.
print(numbers[-1]) # what it does here it will start accessing/counting elements from the last item of the string
print(numbers[::-2]) # reverse jumping/accessing elements of string by step of 2  ans is(9753)

