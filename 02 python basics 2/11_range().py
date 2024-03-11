# range ()

print(range(100)) # it prints range(0, 100), by default it starts from 0

# to iterate over a range or take out each number as a variable we can simply use item, i, number or whatever we want to write
for i in range(100):
    print(i)
# here letter i refers to the index of the number
# also remember it starts from zero by default if we didn't mention the starting number of the range
# it will print from 0 to 99, because it follows stop point (n-1)which is (100-1)

# range function also takes step to jump over the sequence of your choice
print("range function with step")
for i in range(0, 10, 1):  # it will print list 10 times with respective step of 1
    print(list(range(11,20))) # here list is generated for range function items