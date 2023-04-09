# Majuscule

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


def first_uppercase(string):
    result = ""
    first_letter = True
    for x in range(0, len(string)):
        if string[x] == " ":
            result += string[x]
            first_letter = True
        else:
            if first_letter:
                result += uppercase(string[x])
                first_letter = False
            else:
                result += string[x]

    print(result)


try:
    argument = sys.argv[1]

    if isdigit(argument):
        print("erreur.")
        sys.exit()
    else:
        first_uppercase(argument)

except IndexError:
    print("erreur.")
    sys.exit()
