#!/bin/python3

import math
import os
import random
import re
import sys

def is_leap(year):
    leap = False
    
    # Check if year is divisible by 4
    if year % 4 == 0:
        leap = True
        # Check if year is divisible by 100
        if year % 100 == 0:
            leap = False
            # Check if year is divisible by 400
            if year % 400 == 0:
                leap = True
    
    return leap

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))