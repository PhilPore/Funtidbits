#!/bin/python3
#https://www.geeksforgeeks.org/subset-no-pair-sum-divisible-k/
#https://www.hackerrank.com/challenges/non-divisible-subset/problem
"""

For any number K, the sum of 2 values (A & B) is evenly divisible by K if the sum of the remainders of A/K + B/K is K. 
There is also a special case where both A & B are evenly divisible, giving a sum of 0.) For any such remainder, there is 1 and only 1 other remainder value 
which will make a sum divisible by K.

Example: with K of 5, remainder pairs are 1+4 & 2+3. Given the numbers with a remainder of 1, they can't be paired with ANY of the numbers with remainder 4 (and vice versa). 
So, for the number of values in the resultant set, choose the larger of values with remainder 1 vs. values with remainder 4. Choose the larger set of remainder 2 vs remainder 3.

For the special case where remainder is 0, given the set of all values which are individually divisible by K, they can't be paired with any others. 
So, at most 1 value which is evenly divisible by K can be added to the result set.

For even values of K, the equal remainder is simular to the 0 case. For K = 6, pairs are 1+5, 2+4, 3+3. 
For values with remainder 3, at most one value can be added to the result set.


"""
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
        mat[k//2] = min(mat[k//2],1) #due to the sum of 2 numbers being i and k-i we need to split the middle for an even number due to it being counted twice
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
