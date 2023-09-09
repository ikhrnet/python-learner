#!/usr/bin/env python

pin = '1111'

invalid = pin[0] == pin[1] == pin[2] == pin[3]

if invalid:
    print("You can't use the same number for all four digits.")
        #-> You can't use the same number for all four digits.
