#This is to find the amount of numbers there are between two sets. I had to look around for some ways of finding the GCD, though in the end I got it

def computeGCD(hi, lo): #euclidian approach. modular arithmetic
   #e=0
   while(lo):
    #print(e) 
    #e+=1
    #print("x{} | y{} ".format(hi,lo))   
    hi, lo = lo, hi % lo 
    
   #print("xo {} | yo {}".format(hi,lo)) 
   return hi 
def getTotalX(a, b):
    #a is our min range, b is the max.
    aprod = a[0] #we need the lcf
    for i in range(1,len(a)):
        #print(aprod*a[i])
        aprod = (aprod*a[i])//computeGCD(a[i],aprod) #LCF
    count = 0
    bprod = b[0] #LCF for b
    for i in range(1,len(b)):
        bprod = computeGCD(b[i],bprod)
    factor = 1
    print(bprod)
    mb = min(b)
    while (aprod*factor) <= mb:
        print(aprod*factor)
        if bprod%(aprod*factor) == 0:
            count+=1
        factor+=1
    
    return count
