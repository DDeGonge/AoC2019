__version__ = '0.1.0'

import os
import sys
import numpy as np

NARGS = 3

def Read_File(path):
    with open(path, 'r') as f:
        rawdata = f.read().split('\n')
        return [int(i) for i in rawdata]

def Calc_Fuel(w):
    fuel = int(w/3) - 2
    totalFuel = fuel
    while True:
        newfuel = int(fuel/3) - 2
        if newfuel <= 0:
            return totalFuel
        else:
            totalFuel += newfuel
            fuel = newfuel

def main(inPath):
    # Get IntCode
    inputs = Read_File(inPath)
    totalFuel = 0
    for w in inputs:
        totalFuel += Calc_Fuel(w)
        print(Calc_Fuel(w))

    print(totalFuel)
    return

if __name__ == "__main__":
    main(sys.argv[1])