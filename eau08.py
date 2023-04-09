# Chiffres only

import sys


def number_only(string):
    string = str(string)
    is_number = True
    if "0" <= string <= "9":
        print(is_number)
    else:
        is_number = False
        print(is_number)

try:
    argument = sys.argv[1]
    number_only(argument)
except TypeError:
    print("erreur.")
    sys.exit()
except NameError:
    print("erreur.")
    sys.exit()
except IndexError:
    print("erreur.")
    sys.exit()