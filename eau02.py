# Paramètres à l’envers

import sys


def revers_parameter(*args):
    if not sys.argv[1:]:
        print("Erreur.")
        sys.exit()

    words = [i for i in args]
    for n in words[::-1]:
        print(n)


arguments = sys.argv[1:]
revers_parameter(*arguments)
