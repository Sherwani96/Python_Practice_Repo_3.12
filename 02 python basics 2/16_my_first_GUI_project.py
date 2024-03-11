# Exercise

picture = [
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 1, 1, 1, 0, 0],
    [0, 1, 1, 1, 1, 1, 0],
    [1, 1, 1, 1, 1, 1, 1],
    [0, 0, 0, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 0, 0]
]

# every list in picture is a list of pixels
# combined list here is called image

for image in picture:
    for pixel in image:
        if (pixel):
            print('*', end='') # here it will print a star for each pixel in place of 1
        else:
            print(' ', end='') # here it will print a space for each pixel in place of 0
    print('') # here it will print a new line for each list


