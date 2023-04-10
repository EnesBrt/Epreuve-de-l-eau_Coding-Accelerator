# Index wanted

import sys


def research_index(array, string):
    table = [i for i in array]
    for n in range(0, len(table)):
        if string == array[n]:
            print(n)
            break
    else:
        print(-1)


argument_one = sys.argv[1:-1]  # Get all arguments except the last one
argument_two = sys.argv[-1]
research_index(argument_one, argument_two)
