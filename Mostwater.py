def ContwithMostWater(hght):
    l = 0
    r = len(hght)-1
    maxarr = -1
    while l != r:
        distance = r-l
        tempval = min(hght[l],hght[r])*distance
        #we want to close in on what might have the most area, so we want to maximize this
        if hght[l] < hght[r]:
            l+=1
        else:
            r-=1
        if tempval > maxarr:
            maxarr = tempval
    return maxarr
containers = [1,8,6,2,5,4,8,3,7]
maxarea = ContwithMostWater(containers)
print(maxarea)