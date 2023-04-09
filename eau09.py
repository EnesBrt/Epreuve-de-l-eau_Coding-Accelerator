# Entre min et max

import sys


def min_max(a, b):
    for x in range(a, b + 1):
        print(x, end=" ")

    if a > b:
        for x in range(b, a + 1):
            print(x, end=" ")

try:
    if len(sys.argv) > 3:
        print("error")
    else:
        argument_one = int(sys.argv[1])
        argument_two = int(sys.argv[2])
        min_max(argument_one, argument_two)
except TypeError:
    print("error")
except ValueError:
    print("error")
except IndexError:
    print("error")
