# Tri à bulle

import sys

def sorting(number):
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
    sorting(argument)
except ValueError:
    print("error")
    sys.exit()
except IndexError:
    print("error")
    sys.exit()