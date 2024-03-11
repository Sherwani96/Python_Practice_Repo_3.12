# exercise make function to find highest even number in the provided list


def highest_even(li):
    even_nums = []
    for item in li:
        if item % 2 == 0:
            even_nums.append(item)
    return max(even_nums)

print(highest_even([10,2,3,4,8,11]))

# using return statement in for loop in function will only return the 1st value whether it is greater or not

print(5 % 2) # it returns remainder, so for ic case of finding even or odd we use %
print(5 // 2) # it returns quotient