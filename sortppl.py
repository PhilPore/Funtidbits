#https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/submissions/
def groupThePeople(groupSizes): #o(n) solution I think, with some space. When a part of the dictionary reaches capacity i simply append the array in said part to the solution array, and then clear that section of the dictionary for space. 
#This means I do not need to do another function to see if there is anything left behind
        groupdict = {}
        arr = []
        for i in range(len(groupSizes)):
            k = groupSizes[i]
            if k not in groupdict:
                groupdict[k] = []
            groupdict[k].append(i)
            #print(groupdict)
            if len(groupdict[k]) == k:
                
                arr.append(groupdict[k])
                #print(arr)
                groupdict[k] = []
                
        return arr
 print(groupThePeople([3,3,3,3,3,1,3]))
