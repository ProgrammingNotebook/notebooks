import unittest

#-------------------------
# Binary Search Algorithm
#-------------------------

def binary_search(list, element):

    length = len(list)
    index = int(length / 2)


    print(element, list, length, index)

    if (length == 0): return -1
    elif (list[index] == element): return index
    elif (list[index] < element): return binary_search(list[index + 1:], element)
    else: return binary_search(list[:index], element)


xs = [2, 3, 5, 7, 11, 13, 17, 23, 29, 31, 37, 43, 47, 53]

# print(binary_search(xs, 20) == -1)
# print(binary_search(xs, 99) == -1)
# print(binary_search(xs, 1) == -1)

for (i, v) in enumerate(xs):
    print(binary_search(xs, v) == i)
