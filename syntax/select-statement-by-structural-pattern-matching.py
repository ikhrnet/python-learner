#!/usr/bin/env python

n = 6

match n:
    case 2 | 3 | 5 | 7:
        print(f'{n} is a prime number.')
    case 0 | 1 | 4 | 6 | 8 | 9:
        print(f'{n} is not a prime number.')        #-> 6 is not a prime number.
    case _:
        print(f'{n} is out of range in this test.')
