def closest_string(word1, word2):
    if len(word1) != len(word2) or set(word1) != set(word2):
            return False
        #lets use sets! they get all the unique characters! and we can use them to get a count!
    w_1 = [word1.count(i)  for i in set(word1)]
    w_1.sort()
    w_2 = [word2.count(i)  for i in set(word2)]
    w_2.sort()
    return w_1 == w_2


    
    '''
        freq_list1 = OrderedDict()
        freq_list2 = OrderedDict()
        for i in range(len(word1)):
            if word1[i] not in freq_list1:
                freq_list1[word1[i]] = 1
            elif word1[i] in freq_list1:
                freq_list1[word1[i]]+=1
            
            if word2[i] not in freq_list2:
                freq_list2[word2[i]] = 1
            elif word2[i] in freq_list2:
                freq_list2[word2[i]]+=1
        print(freq_list1)
        print(freq_list2)
        #make two lists sorted by  frequencies
        freq_a = []
        freq_b = []
        
        for key1 in freq_list1:
            if key1 not in freq_list2:
                return False
            freq_a.append(freq_list1[key1])
        for key2 in freq_list2:
            freq_b.append(freq_list2[key2])
        freq_a.sort()
        freq_b.sort()
        print(freq_a)
        print(freq_b)
        for i in range(len(freq_a)):
            if freq_a[i] != freq_b[i]:
                return False
                
        return True
            
            
        '''