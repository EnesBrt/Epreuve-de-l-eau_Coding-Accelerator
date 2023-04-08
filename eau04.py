# Prochain nombre premier

import sys


def prime(number):
    try:
        number = int(number)
        number = number + 1
        while True:

            square_root = number ** (1 / 2)
            if number <= 1:
                number += 1
            elif number == 2:
                print(number)
                break
            elif number > 2 and number % 2 == 0:
                number += 1
            else:
                is_prime = True
                for n in range(3, int(square_root) + 1, 2):
                    if number % n == 0:
                        is_prime = False
                        break

                if is_prime:
                    print(number)
                    break
                else:
                    number += 1
    except ValueError:
        print(-1)


try:
    argument = sys.argv[1]
    prime(argument)
except IndexError:
    print(-1)
