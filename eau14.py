# Par ordre Ascii

import sys


def isdigit(s):
    for x in s:
        if not ('0' <= x <= '9'):
            return False
    return True


def ascii_order(string):
    strings = string.split()
    for n in range(len(strings)):
        for x in range(n + 1, len(strings)):
            if ord(strings[n][0]) > ord(strings[x][0]):
                strings[n], strings[x] = strings[x], strings[n]

    sorted_words = " ".join(i for i in strings)

    print(sorted_words)




try:
    argument = sys.argv[1:]
    if isdigit(" ".join(argument)):
        print("error")
    else:
        ascii_order(" ".join(argument))
except ValueError:
    print("error")
    sys.exit()
except IndexError:
    print("error")
    sys.exit()