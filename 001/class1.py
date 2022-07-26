#!/bin/python3

"""
Given an integer, N, perform the following conditional actions:

If N is odd, print Weird
If N is even and in the inclusive range of 2 to 5, print Not Weird
If N is even and in the inclusive range of 6 to 20, print Weird
If N is even and greater than 20, print Not Weird
"""

import math
import os
import random
import re
import sys

def par_impar(numero):
    if numero % 2 != 0:
        print("Weird")
        return "Weird"
    elif numero >= 6 and 20 >= numero:
        print("Weird")
        return "Weird"
    else:
        print("Not Weird")
        return "Not Weird"


# if __name__ == '__main__':
#     n = int(input("").strip())
#
#     par_impar(n)
