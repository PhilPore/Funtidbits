def saveThePrisoner(n, m, s): #n: number of prisoners, m: number of candies, s: starting pos. Return the prisoner thats going to get the bad candy which is the last one
    if m == 1:
        return s
    return (s-1+m-1)%n+1 #math it up. s-1 is the index of the starting chair, m-1 accounts for the first guy taking the candy. We're working indexes here, %n to wrap it around so 
    we dont go over number of prisoners, and then +1 to bring it to actual prisoner numbers.  
    
print(saveThePrisoner(7,19,5)
