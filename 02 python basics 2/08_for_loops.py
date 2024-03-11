# loops allows us to run lines of code repeatedly
# for loops allows us to iterate over anything that has a collection of items

for item in (1, 2, 3, 4, 5):
    print(item)
    print(item)
    print(item)
print(item)  # at that time while iterating the item, in th tuple 5 was left, so in the last 5 will be printed

# we can also nest loops within a loops
for item in (1, 2, 3, 4, 5):
    for x in ['a', 'b', 'c']:  # what it does here it will exit the loop when there is no item left
        print(item, x)
# then it will move to the outer loop take the item and move to inner loop and will be in the loop until there is no item left
