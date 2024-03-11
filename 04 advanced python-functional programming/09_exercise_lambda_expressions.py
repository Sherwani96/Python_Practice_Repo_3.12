#  exercise


# squares
my_list = [5, 4, 3]

squares_list = list(map(lambda item: item ** 2, my_list))

print(squares_list)

# list sorting
unsorted_li = [(0, 2), (4, 3), (9, 9), (10, -11)]

unsorted_li.sort(key=lambda x: x[1])

print(unsorted_li)
