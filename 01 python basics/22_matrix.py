# matrix
# matrices are commonly used in image processing and in machine learning

# matrix below is a 2D array
matrix = [            # <-- the main array
    [1, 2, 3],        # <-- the sub array
    [4, 5, 6],        # <-- the sub array
    [7, 8, 9]         # <-- the sub array
]

print(matrix)

# accessing elements
print(matrix[1][2]) # array on 1st index [1] which is an entire array [1, 2, 3] in main array(access the element on 2nd index [2])  answer is 6
print(matrix[0][0]) # array on 0th index [0] which is an entire array [4, 5, 6] in main array(access the element on 0th index [0]) answer is 1
print(matrix[2][1]) # array on 2nd index [2] which is an entire array [7, 8, 9] in main array(access the element on 1st index [1]) answer is 8