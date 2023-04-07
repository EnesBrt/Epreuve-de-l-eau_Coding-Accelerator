# Suite de Fibonacci

import sys


def fibonacci(n):
    try:
        n = int(n)
        fibo = [0, 1]
        a = fibo[0]
        b = fibo[1]

        for x in range(len(fibo) - 1, n):
            c = a + b
            a = b
            b = c
        print(c)
    except UnboundLocalError:
        print(-1)
    except ValueError:
        print(-1)


argument = sys.argv[1]
fibonacci(argument)
