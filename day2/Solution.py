__version__ = '0.1.0'

import os
import sys
import numpy as np

NARGS = 3

def Read_Intcode(path):
    with open(path, 'r') as f:
        rawdata = f.read()
        vals = rawdata.split(',')
        return [int(i) for i in vals]

def Get_Addr0(intCode):
    # Parse IntCode
    index = 0
    while index < len(intCode):
        cmd = intCode[index]
        args = intCode[index + 1:index + NARGS + 1]
        
        if cmd == 1:
            intCode[args[2]] = intCode[args[0]] + intCode[args[1]]
        elif cmd == 2:
            intCode[args[2]] = intCode[args[0]] * intCode[args[1]]
        elif cmd == 99:
            return intCode[0]
        else:
            return -1

        index += (NARGS + 1)

def main(inPath):
    # Get IntCode
    orig_intCode = Read_Intcode(inPath)

    target = 19690720
    for noun in range(0,100):
        for verb in range(0,100):
            intCode = np.array(orig_intCode)
            intCode[1] = noun
            intCode[2] = verb
            sol = Get_Addr0(intCode)
            if sol == target:
                print('noun: {}, verb: {}'.format(noun,verb))
    
    return

if __name__ == "__main__":
    main(sys.argv[1])