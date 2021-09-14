#https://www.hackerrank.com/challenges/bigger-is-greater/problem

#NEXT BIGGEST lexically 
#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'biggerIsGreater' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING w as parameter.
#

def biggerIsGreater(w):
    # Write your code here
    
    
    w2 = list(w)
    l = len(w2)-1
    while l > 0 and w2[l-1] >= w2[l]:
        l-=1
    if l <= 0:
        return "no answer"
    
    r = len(w2)-1
    while w2[r] <= w2[l-1]:
        r-=1
    w2[r],w2[l-1] = w2[l-1],w2[r]
    
    w2[l:] = w2[l:][::-1]
    return "".join(w2)

    arr = list(w)
    # Find non-increasing suffix
    i = len(arr) - 1
    while i > 0 and arr[i - 1] >= arr[i]:
        i -= 1
    if i <= 0:
        return "no answer"
    
    # Find successor to pivot
    j = len(arr) - 1
    while arr[j] <= arr[i - 1]:
        j -= 1
    arr[i - 1], arr[j] = arr[j], arr[i - 1]
    
    # Reverse suffix
    arr[i : ] = arr[len(arr) - 1 : i - 1 : -1]
    return "".join(arr)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()
