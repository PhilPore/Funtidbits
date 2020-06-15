class minheap:
    def __init__(self):
        self.size = 0 #typically in other languages where you need to define an array size, 
                    #size is used to make the heap in question.
        self.heap = []
    #equations:
    '''
    Arr[(i-1)/2]	Returns the parent node
    Arr[(2*i)+1]	Returns the left child node
    Arr[(2*i)+2]	Returns the right child node
    '''
    def getparentind(self, childind):
        return((childind-1)//2)
    def getLchildind(self,parentind):
        return((parentind*2)+1)
    def getRchildind(self, parentind):
        return((parentind*2)+2)
   
    #now we need to check if it exists so we have to use our LEN function and bools. COOL!
    def hasparent(self,index):
        return self.getparentind(index) >= 0
    def hasLchild(self,index):
        return self.getLchildind(index) < self.size
    def hasRchild(self,index):
        return self.getRchildind(index) < self.size
    

    #get our values associated with the index. Nice.
    def getparent(self,childind):
        return (self.heap[self.getparentind(childind)])
    def getLchild(self, parentind):
        return (self.heap[self.getLchildind(parentind)])
    def getRchild(self,parentind):
        return (self.heap[self.getRchildind(parentind)])

    #some helper functions
    def swap(self,a,b):
        temp = self.heap[a]
        self.heap[a] = self.heap[b]
        self.heap[b] = temp
        #print("{} - {}".format(a,b))
    def ensurecap(self):
        if self.size == len(self.heap):
            self.heap.append(None)
    '''
    as a note, in some languages we'd have an ensure capacity function added in to make sure we are not going over. 
    If we are, we have to copy it over to another array. This is how arraylists are made. Cool! 
    '''
    #our useful functs

    def peak(self):
        if self.size == 0:
            raise ValueError("Nothing in heap")
        return self.heap[0]
    

    def heapifydown(self):
        ind = 0
        while(self.hasLchild(ind)):
            smalchildind = self.getLchildind(ind)
            if (self.hasRchild(ind) and self.getRchild(ind) < self.getLchild(ind)):
                smalchildind = self.getRchildind(ind)
            if self.heap[ind] < self.heap[smalchildind]:
                break
            else:
                self.swap(ind,smalchildind)
                index = smalchildind




    def heapifyup(self):
        ind = self.size-1
        
        while(self.hasparent(ind) and self.getparent(ind) > self.heap[ind]):
            print("Here")
            print(self.getparentind(ind))
            print("ereH")
            self.swap(self.getparentind(ind),ind)
            print(self.heap[self.getparentind(ind)])
            print(self.heap[ind])
            ind = self.getparentind(ind)

    def poll(self):
        if self.size == 0:
            raise ValueError("Nothing in heap")
        oldhead = self.heap[0]
        self.heap[0] = self.heap[self.size-1]
        self.size-=1
        self.heapifydown()
        return oldhead

    def insert(self,value):
        print("Val:{}".format(value))
        if (self.size == 0):
            self.heap.append(value)
            self.size+=1
        else:
            self.ensurecap()
            self.heap[self.size] = value
            self.size+=1
            self.heapifyup()
            

heap1 = minheap()
heap1.insert(10)
heap1.insert(15)
heap1.insert(20)
heap1.insert(8)
heap1.insert(17)
for i in range(heap1.size):
    print(heap1.heap[i], end =" ")
x = heap1.poll()
print()
print(x)
'''
possibly useful for heapsort 0 . 0
x = heap1.poll()
print(x)
x = heap1.poll()
print(x)
x = heap1.poll()
print(x)
'''

for i in range(heap1.size):
    print(heap1.heap[i], end =" ")
print(heap1.heap)