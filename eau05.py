# String dans string

import sys


def string_in_string(string_one, string_two):
    is_in = False
    for n in string_one:
        if string_two in string_one:
            is_in = True
    print(is_in)


try:
    argument_one = sys.argv[1]
    argument_two = sys.argv[2]
    string_in_string(argument_one, argument_two)

except IndexError:
    print("erreur.")
