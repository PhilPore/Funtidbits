import math
import os
import random
import re
import sys

#
# Complete the 'minimumBribes' function below.
#
# The function accepts INTEGER_ARRAY q as parameter.
#

def minimumBribes(q):
    # Write your code here
    l = len(q)-1
    tot_bribes = 0
    for i in range(l,-1,-1):
        if (q[i]-(i+1) > 2): #means if theres a bribe and its greater than 2 we got a problem.
            print("Too chaotic")
            return
        j = max(0,(q[i]-2)) #ensure we dont go negative
        while j < i:
            #print("{}={}".format(q[i],q[j]))
            #print("{}-{}".format(i,j))
            if q[j] > q[i]: #How many people needed to bribe their way to get ahead. Should know by the value. 
                #print("F")
                tot_bribes+=1
            j+=1
    #print(tot_bribes)
        
        
        
            
    print(tot_bribes) 
