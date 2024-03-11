# enumerate

# what enumerate() does is it takes out objet and index it. and helps to access it using index number
# remember you pass an iterables to enumerate() function

for i, char in enumerate('hello!'):
    print(i, char)


# below we are going to access the index of a particular number from list
for i, char in enumerate(list(range(1,10))):
    if char == 5:
        print(f'the index of 5 is {i}')


for i, char in enumerate(list('hello there!!')):
    print(i, char)