class Solution:
    def countPrimes(self, n: int) -> int:
        #sieve of eratoshenes, mark all composites
        count = 0
        prime_list = [True for i in range(n)]
        if n <= 2:
            return 0
        
        for i in range(2,int(sqrt(n))+1):
            inc = 0
            p = i*i
            if prime_list[i]:
                while p < n:
                    #print(inc*i)
                    #f prime_list[inc*i] == False:
                        #reak
                    prime_list[p] = False
                    p+=i
        #print(prime_list)
        for i in range(2,n):
            if prime_list[i]:
                count+=1
        #note: if prime list was integers 0 and 1, we could have done a sums return and gotten the same answer
        return count
