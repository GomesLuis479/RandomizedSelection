# An implementation of the randomised selection algorithm
# with average running time of O(n).
# select(array, n) returns the nth smallest element in an array
# where n >= 1.
# Also referred to as the nth order statistic.

import random


def swap(arr, i, j):
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


def selector(arr, start, end, statistic):

    if start == end:
        return arr[start]

    # Randomly choose a pivot.
    # Pivot needs to be in the first position of the
    # array for partitioning. Thus the swap.
    random_pos = random.randint(start, end)
    swap(arr, random_pos, start)
    pivot = arr[start]

    # Perform partitioning about pivot.
    i = start
    for j in range(start+1, end+1):
        if arr[j] <= pivot:
            i = i + 1
            swap(arr, i, j)

    swap(arr, start, i)
    # i is the index of the pivot after partitioning.

    relative_statistic_of_pivot = i - start

    if relative_statistic_of_pivot == statistic:
        return arr[i]

    if relative_statistic_of_pivot > statistic:
        return selector(arr, start, i-1, statistic)

    if relative_statistic_of_pivot < statistic:
        return selector(arr, i+1, end, statistic-(relative_statistic_of_pivot + 1))


def select(arr, statistic):
    # Make a copy to avoid in place changes.
    # statistic - 1 is passed to the  recursive function
    # to make the statistic 0 indexed
    # the user is expected to enter the nth statistic: n >= 1.

    arr_new = arr[:]
    return selector(arr_new, 0, len(arr_new)-1, statistic-1)


test_array = [i for i in range(-100, 100)]
random.shuffle(test_array)

# result is generated by querying the nth smallest element
# in shuffled test_array.
# result must be equal to the ordered test array.

result = []
for i in range(len(test_array)):
    result.append(select(test_array, i+1))

print("result == ordered test array? =", result == sorted(test_array))
