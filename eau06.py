# Majuscule sur deux

import sys


def isdigit(s):
    for x in s:
        if not ('0' <= x <= '9'):
            return False
    return True


def uppercase(string):
    result = ""
    a = 97
    z = 122
    for n in string:
        n = ord(n)
        if a <= n <= z:
            upper = n - 32
            upper = chr(upper)
            result += upper
        else:
            result += chr(n)
    return result


def to_upper(string):
    result = ""
    non_space_index = 0
    for x in range(0, len(string)):
        if string[x] == " ":
            result += string[x]
        else:
            if non_space_index % 2 == 0:
                result += uppercase(string[x])
            else:
                result += string[x]
            non_space_index += 1

    print(result)


argument = sys.argv[1]

if isdigit(argument):
    print("erreur.")
else:
    to_upper(argument)

