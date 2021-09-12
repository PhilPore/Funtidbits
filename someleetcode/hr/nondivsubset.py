#!/bin/python3
#https://www.geeksforgeeks.org/subset-no-pair-sum-divisible-k/
#https://www.hackerrank.com/challenges/non-divisible-subset/problem
import math
import os
import random
import re
import sys

#
# Complete the 'nonDivisibleSubset' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY s
#

def nonDivisibleSubset(k, s):
    # Write your code here.
    mat = [0 for i in range(k)] #st ore modulo
    for i in range(len(s)):
        print(s[i]%k,end=" ")
        mat[s[i]%k]+=1 #find the frequency of each modulo in range
    print(mat)
    if (k%2) == 0:
        mat[k//2] = min(mat[k//2],1)
    res = min(1,mat[0])
    print(k//2+1)
    for i in range(1,k//2+1):
        print("{} vs {} = {} vs {}".format(i,k-i,mat[i],mat[k-i]))
        res+=max(mat[i],mat[k-i])
    return res 
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)

    fptr.write(str(result) + '\n')

    fptr.close()
