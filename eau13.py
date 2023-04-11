# Tri par sélection

import sys


def selection_sort(number):
    array = [int(i) for i in number]
    for n in range(0, len(array)):
        for x in range(n, len(number)):
            if array[n] > array[x]:
                array[n], array[x] = array[x], array[n]

    numbers = " ".join(str(i) for i in array)
    print(numbers)
    return numbers


try:
    argument = sys.argv[1:]
    selection_sort(argument)
except ValueError:
    print("error")
    sys.exit()
except IndexError:
    print("error")
    sys.exit()
