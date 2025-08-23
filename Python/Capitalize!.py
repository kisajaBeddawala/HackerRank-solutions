import math
import os
import random
import re
import sys

def solve(s):
    names = s.split(" ")
    for i in range(len(names)):
        names[i] = names[i].capitalize()
    
    return " ".join(names)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = solve(s)

    fptr.write(result + '\n')

    fptr.close()
