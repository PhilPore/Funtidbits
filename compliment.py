
import sys

#find a pair such that a+b+c = 0
#unordered set
'''
def threewaycomp(s):
    s.sort()
    compdict ={}
    for a in range(len(s)):
        
      for b in range(len(s)):
            #print("{} {}\n".format(s[a],s[b]))
            if a != b:
                #print("{} {}".format(a,b))
                compdict[-(s[a]+s[b])] = [s[a],s[b]]
            
    print(compdict)       

    unidict = {}
    sol_set = []
    for c in s:
        print(c)
        #print(c)
        if c in unidict:
            unidict[c] +=1
        else:
            unidict[c] = 1
        if c in compdict and unidict[c] == 1 and sorted([compdict[c][0], compdict[c][1], c]) not in sol_set:
            print("{} = {}, {}".format(c, s.count(c),c in compdict[c]))
            if c in compdict[c] and s.count(c) == 1:
                continue
            print("{} {} {}".format(compdict[c][0], compdict[c][1], c))
            sol_set.append(sorted([compdict[c][0], compdict[c][1], c]))
    print(sol_set)
'''         
def divisibleSumPairs(n, k, ar): #initially did this O(n^2). This is now O(n+k), O(k), had to look up external resources to optimize. Thankfully this reminded me buckets were a thing hah.
    count = 0
   #we use buckets based off modulo k
    buckets = [0 for i in range(k)] #spans from 0 to k-1
    for i in range(len(ar)):
        comp = ar[i]%k #as to fit the buckjets
        print(ar[i])
        print(comp)
        print(k-comp) #we need this to find what will equal k from our comp
        print("..")
        count+=buckets[(k-comp)%k] #insert the value from the bucket thats needed for our compliment. 
        #Modulo is to ensure things divisible by it go to 0 (meaning its already divisible)
        buckets[comp]+=1 #increment our bucket with the modded index value. 
        #Meaning we it exists. This is helpful when we find another comp value that uses the previous index value. 
        # #Since there is a value in there,we just add that to count. #
        # Presumably to account for 1+2 and 2+4 (if 4 was already found)
    return count

def threescomp(n):
    sol_set = []
    #s = 0
    #e = len(n)-1
    n.sort()
    print(n)
    for i in range(len(n)-2):
        if i==0 or (i > 0 and n[i] != n[i-1]):
            comp = -(n[i])
            s = i+1
            e = len(n)-1
            while s < e: 
                #we use l r pointers to find the compliment, 
                # closing in on each other. Its effectively a high and low value.
                if n[s]+n[e] < comp:
                    s+=1
                elif n[s]+n[e] > comp:
                    e-=1
                else:
                    sol_set.append(sorted([n[i],n[s],n[e]]))
                    #when we find the solution for this set, we want to 
                    # make sure the next time we look we dont hit a duplicate 
                    # so, we iterate through until no duplicate is found and move both pointers closer
                    #logically speaking you wont recycle the same l r numbers to find a compliment, if you find 0,2 for -2
                    # then its likely you wont use 0, or 2 for that compliment again  
                    while s < e and n[s] == n[s+1]:
                        s+=1
                    while s < e and n[e] == n[e-1]:
                        e-=1

                    s+=1
                    e-=1
    return sol_set


            

x = [1,1,-1, -2,-1,0]
y = [-1,0,1,2,-1,-4]
z = [3,0,-2,-1,1,2]

ar = [1, 3, 2, 6, 1, 2]
print(divisibleSumPairs(6,3,arr))
#threewaycomp(x)
pre = threescomp(y)
print(pre)