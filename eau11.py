# Différence minimum absolue

import sys


def sort(number):
    for n in range(0, len(number)):
        for x in range(n, len(number)):
            if number[n] > number[x]:
                number[n], number[x] = number[x], number[n]

    return number


def find_difference(number):
    number = [int(i) for i in number]
    sorted_number = sort(number)
    results = []
    for n in range(len(sorted_number)):
        for m in range(n + 1, len(sorted_number)):
            result = abs(sorted_number[n] - sorted_number[m])
            results.append(result)

    minimum = results[0]
    for x in results:
        if x < minimum:
            minimum = x

    print(minimum)


try:
    argument = sys.argv[1:]
    find_difference(argument)
except ValueError:
    print("error")
    sys.exit()
except IndexError:
    print("error")
    sys.exit()
