# Tri à bulle

import sys


def bubble_sort(number):
    array = [int(i) for i in number]
    for n in range(0, len(array)):
        for x in range(0, len(array) - n - 1):
            if array[x] > array[x + 1]:
                array[x], array[x + 1] = array[x + 1], array[x]

    numbers = " ".join(str(i) for i in array)
    print(numbers)
    return numbers


try:
    argument = sys.argv[1:]
    bubble_sort(argument)
except ValueError:
    print("error")
    sys.exit()
except IndexError:
    print("error")
    sys.exit()
