"""
We define P to be a permutation of the first  natural numbers in the range [1,N]. Let POS[I] denote the value at position I in permutation P using 1-based indexing.

P is considered to be an absolute permutation if |POS[I]-I|=K holds true for every I IN [1,N].

Given N and K, print the lexicographically smallest absolute permutation P. If no absolute permutation exists, print -1.

"""


def absolutePermutation(n, k):
    # Write your code here
    #rn = range(1,n+1)
    used = []
    arr = [i+1 for i in range(n)]
    if k == 0:
        return arr
    #print(arr)
    if n%(k*2) != 0:
        print(-1)
        return [-1]
    
    for i in range(len(arr)):
        if (i//k)%2 == 0:
            arr[i] = arr[i]+k
        else:
            arr[i] = abs((i+1)-k)
    return arr
