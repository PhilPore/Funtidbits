#convert an  integer into binary

import sys

def convbin(val):
    n = 0
    bin_val = ""
    while (1 << n) <= val:
        bin_val = str(int(bool(1<<n & val)))+bin_val
        n+=1
    print(bin_val)


convbin(int(sys.argv[1]))
