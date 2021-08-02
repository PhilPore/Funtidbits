import string

def Pali_Perm(stri):
    char_freqs = {}
    true_len = 0
    for i in stri:
        if i.isalnum():
            true_len+=1
            if i.lower() not in char_freqs:
                char_freqs[i.lower()] = 1
            else:
                char_freqs[i.lower()]+=1
    print(char_freqs)
    print(true_len)
    can_odd = True
    if true_len%2 == 0:
        can_odd = False
    for key in char_freqs:
        if char_freqs[key]%2 == 1 and not can_odd:
            return False
    
    
    return True
    
def One_away(str1, str2):
    #page 201 has a similar solution that uses o(1) space.
    #to replicate
    if abs(len(str1)-len(str2)) > 1:
        return False
    min_str = str1 if len(str1) < len(str2) else str2
    max_str = str2 if len(str1) < len(str2) else str1
    ind1, ind2 = 0,0
    differ = False
    while ind1 < len(min_str) and ind2 < len(max_str):
        if min_str[ind1] != max_str[ind2]:
            if differ:
                return False
            differ = True
            if len(max_str) == len(min_str):
                ind1+=1
        else:
            ind1+=1
        ind2+=1
    return True 


    '''
    if abs(len(str1)-len(str2)) > 1:
        return False
    differ = abs(len(str2)-len(str2))
    #three operations possible: insert, remove, replace
    main_str = None
    check_str = None
    str_arr = None
    if len(str1) > len(str2):
        main_str = list(str1) 
        check_str = list(str2)
        str_arr = ['' for i in range(len(main_str))]

    else:
        main_str = list(str2)
        check_str = list(str1)
        str_arr = ['' for i in range(len(main_str))]

    print(f"{main_str}, {check_str}")
    diff = 0
    str_arr = ['' for i in range(len(main_str))]
    for i in range(len(check_str)):
        
        if check_str[i] is main_str[i]:
            str_arr[i] = check_str[i]
        elif check_str[i] is main_str[i+1]:
            str_arr[i+1] = check_str[i]
    print(str_arr)

    for i in str_arr:
        if i is '':
            diff+=1
            if diff > 1:
                return False



    return True        
'''

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        true_len = len(matrix)*len(matrix[0])
        check_mat = [[False for i in range(len(matrix[0]))] for _ in range(len(matrix))]
        x_bounds = len(matrix[0])
        y_bounds = len(matrix)
        spiral_mat = []
        matrix_trav = 0
        act_x = [1,0,-1,0]
        act_y = [0,1,0,-1]
        x_acc = 0
        y_acc = 0
        action = 0
        for i in range(true_len):
            #print(f"{y_acc},{x_acc}")
            spiral_mat.append(matrix[y_acc][x_acc])
            check_mat[y_acc][x_acc] = True
            c_x = x_acc+act_x[action]
            c_y = y_acc+act_y[action]
            if 0 <= c_x < x_bounds and 0<= c_y < y_bounds and not check_mat[c_y][c_x]:
                x_acc = c_x
                y_acc = c_y
            else:
                action = (action+1)%4
                x_acc+= act_x[action]
                y_acc+= act_y[action]
                
    
            
            
            
        return spiral_mat

def String_Comp(str_arg): #converts strings to a compressed formast to see if the len is shorter
    
    new_str = ""
    char_hold = None
    char_count = 0
    for i in str_arg: #another way to do this would be to look ahead
        '''
        ex of other method

        for i in range(len(str_arg)):
            char_count+=1
            if (i+1 >= len(str_arg) or str_arg[i] != str_arg[i+1]):
                new_str+="{}{}".format(str_arg,char_count)
                char_count = 0

        return  new_str if len(new_str) < len(str_arg) else str_arg

        cleans it up a little more. One less value to worry about
        '''
        if not char_hold:
            char_hold = i
        if i != char_hold:
            
            new_str+="{}{}".format(char_hold,char_count)
            char_count = 0
        char_hold = i
        char_count+=1
    new_str+="{}{}".format(char_hold,char_count)
    return new_str if len(new_str) < len(str_arg) else str_arg

def Rot_Matrix(matrix): 
    #STUDY THIS UNTIL THE CONCEPT IS CLEAR. 
    #EFFECTIVELY CORNER PIECES AND WE NARROW CORNER PIECE DOWN
    '''
    1 2 3 4         13 9 5 1            
    5 6 7 8   --->  14 10 6 2
    9 10 11 12      15 11 7 3
    13 14 15 16     16 12 8 4

    1 2   ->   3 1
    3 4        4 2 

    1 2 3      
    4 5 6
    7 8 9

    to:
    7 4 1
    8 5 2
    9 6 3
    '''
    
    #corner pieces
    #top = 0
    #bottom  = len(matrix)-1
    n = len(matrix)
    range_x = [0,n]
    range_y = [0,n]
    for layer in range(len(matrix)//2):
        first = layer
        last = n - 1 - first
        print(f"{first} {last}")
        for i in range(first, last):
            offset = i - first
            top = matrix[first][i] #top is saved
            print(f"{i} | {offset} | {last-offset}")
            #left -> top
            matrix[first][i] = matrix[last-offset][first]

            #bottom -> left
            matrix[last-offset][first] = matrix[last][last-offset]

            #right -> bottom
            matrix[last][last-offset] = matrix[i][last]

            #top -> right
            matrix[i][last] = top
        
    print(matrix)
            
def fourSum(num1,num2,num3,num4): #all lists. Return number of tuples that make 0
    count = 0
    sum_dict = {}
    sum_dict2 = {}
    for i in range(len(num1)):
        for j in range(len(num2)):
            if num1[i]+num2[j] not in sum_dict:
                sum_dict[num1[i]+num2[j]] = []
                sum_dict[num1[i]+num2[j]].append([num1[i],num2[j]])
            else:
                sum_dict[num1[i]+num2[j]].append([num1[i],num2[j]])
    for i in range(len(num3)):

        for j in range(len(num4)):
            if num3[i]+num4[j] not in sum_dict2:
                sum_dict2[num3[i]+num4[j]] = []
                sum_dict2[num3[i]+num4[j]].append([num3[i],num4[j]])
            else:
                sum_dict2[num3[i]+num4[j]].append([num3[i],num4[j]])


    for key in sum_dict:
        comp = -key
        if comp in sum_dict2:
            print(f"{comp} and {key}")
            count+= len(sum_dict2[comp]) #len(sum_dict2[comp])+len(sum_dict[key])
    print(sum_dict)
    print(sum_dict2)

    return count

def zero_mat(matrix): #if in a row there is a 0, turn  the entire row and column into zero
    arr = {} #holds the values of cols*row affected
    #alternative to making this arr is to have two arrays, one M one N. If the row is true, nullify the entire row.
    #if the column is true nullify the entire column.

    #another interesting method in book, end o page 205 to start of page 207
    #efectively it makes use of the matrix to take up o(1) space. 
    # Checks to see if the first col and row have 0s first, and then checks the rest
    row = [False for i in range(len(matrix))]
    col = [False for i in range(len(matrix[0]))]
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                row[i] = True
                col[j] = True
    
    for k in range(len(matrix[0])):
        if col[k] == True:
            for i in range(len(matrix)):
                matrix[i][k] = 0
    
    for q in range(len(matrix)):
        if row[q] == True:
            for i in range(len(matrix[0])):
                matrix[q][i] = 0
    
    return matrix


    ''' my solution
    for i in range(len(matrix)):
        r = 0
        j = 0
        while r < len(matrix[i]):
            #print(f"{i} {r}")
            #print(matrix)
            #print("--")
            if matrix[i][r] == 0 and (len(matrix)*i+r) not in arr:
                #print(matrix[i][r])
                for k in range(len(matrix[i])): #row
                    matrix[i][k] = 0
                for h in range(len(matrix)):
                    if (h*len(matrix)+r) not in arr:
                        matrix[h][r] = 0
                        arr[h*len(matrix)+r] = 1
                #print(arr)
                break

            r+=1
    
    return matrix
    '''

def string_rot(str1,str2): #compare and see if str2 is a rotation of str1
    start_ind = 0
    if len(str1) > len(str2) or len(str1) < len(str2):
        return False 
    while str1[start_ind] != str2[0]:
        start_ind+=1
    
    for i in str2:
        print(f"{i} vs {str1[start_ind%len(str1)]}")
        if i != str1[start_ind%len(str1)]:
            return False
        start_ind+=1
    return True


def search_rotation(arr, target): 
    nums = arr
    '''returns index of the target, assuming it can be found '''
    #note! has to be done in less than n time
    #idear: technically everything is sorted, just rotated
    #check middle index to see if the values are greater on both sides. 
    # If not, then adjust until you find the proper position. Then  treat it like a normal binary search.
    # treat like circular array. 
    # Note: seeking smaller value: when arr[i-1] > arr[i], we know its not found on this side
    # larger: when arr[i+1] < arr[i], we have a problemo
    #better solution that I found:
    low = 0
    high = len(nums)-1 #see, this would have been smart to do in my solution and probably would have been
    #incredibly effective as it grabs a valid index.
    while(low<=high):
        mid= (low+high)//2 #get the mid index between the upper bound index and lowerbound
        if nums[mid] == target: #did we jackpot?
            return mid
        elif nums[mid] <= nums[high]: #check to see if our value is less than upperbound, 
            #meaning its somewhat sorted
            if nums[mid] < target <=nums[high]: #is mid less  than target and is target <= high val
                low = mid+1 #increment low because we want a higher value for mid
            else:
                high = mid-1 # decrement high so we get a lower value for mid
        elif nums[low]<=nums[mid]: #we are in a rotated area where our mid value is greater than our low index val
            #so naturally, we want to get closer to our lowest point instead
            if nums[low]<=target<nums[mid]:
                high = mid-1
            else:
                low = mid+1
    #base case
    return -1          


    '''
    Solution I made for leetcode problem:
    Works but its not as efficient as I am going to be searching a smidge less than N if the target doesnt exist
    The logic isa the same from the points above. Find a point where it seems nonrotated, and search ala 
    binary from there
    mid = len(nums)//2
        prev = mid if len(nums)%2 == 1 else mid-1
        if len(nums) == 1:
            if nums[0] != target:
                return -1
            return 0
        
        while True:
            print((mid+1)%len(nums))
            if(nums[mid%len(nums)] < nums[(mid+1)%len(nums)]):
                break
            #prev+=1
            mid+=1
        print(mid%len(nums))
        #mid+=1
        #now we do the bin search
        for i in range(len(nums)//2*2):
            if nums[mid%len(nums)] == target:
                return mid%len(nums)
            if nums[mid%len(nums)] < target:
                mid+=1
            else:
                mid-=1
        if nums[mid%len(nums)] == target:
            return mid%len(nums)
        return -1

    '''
    '''
    This is too much
    if arr[0] == target: 
        return 0
    if arr[-1] == target:
        return len(arr)-1
    less_than = True
    mid_point = len(arr)//2
    prev = mid_point-1
    ahead = mid_point+1
    if arr[prev%len(arr)] > arr[mid_point] and arr[mid_point] < arr[ahead%len(arr)]:
        prev = mid_point
        mid_point+=1
        ahead+=1
    new_pointer = mid_point
    
    less_than = False if target > arr[mid_point] else True
    index = 0
    while index < mid_point+1:
        if arr[new_pointer%len(arr)] == target:
            return new_pointer%len(arr)
        if less_than:
            ahead = new_pointer-1
            #if arr[ahead%len(arr)] > arr[new_pointer]: original idea here but ah whateves. might come in handy
            #    return None
            new_pointer-=1
            ahead-=1

        else:
            new_pointer+=1
            #do the if statement if this dont work
        index+=1
    
    return None

    return [prev,mid_point,ahead, [arr[prev], arr[mid_point], arr[ahead]]]'''
def max_window(arr,k):
    ''' a faster method is to use a list that stores relevant values. 
        First fill the list with the first k elements. Terminate all tail values that is less than the ith val'''
    queue = []
    max_win_list = []
    for i in range(k): 
        #kinda sorta get all this but will need to look eitehr tomorrow when i get back or wednesday
        while queue and arr[i] >= arr[queue[len(queue)-1]]:
            #print(f"{arr[i]} {arr[queue[len(queue)-1]]}")
            queue.pop()
        queue.append(i)
    #print(queue)
    for i in range(k, len(arr)):
        max_win_list.append(arr[queue[0]])

        while queue and queue[0] <= i-k: #remove unnecessary indexes.
            queue.pop(0)
        
        while queue and arr[i] >= arr[queue[-1]]:
            queue.pop()
        
        queue.append(i)
    
    max_win_list.append(queue[0])

    return max_win_list
        



    '''K is the window
    max_vals_arr = []
    if len(arr) == 1:
        return arr
    #print(len(arr))
    for i in range(len(arr)-k+1):
        max_val = arr[i]
        for j in range(1,k):
            max_val = arr[i+j] if max_val < arr[i+j] else max_val
        max_vals_arr.append(max_val)
    return max_vals_arr
    
    ind = k-1
    while ind < len(arr):
        l = ind - (k-1)
        r = ind
        m_val = arr[l]
        while l <= r:
            m_val = max(m_val, max(arr[l], arr[r]))
            l+=1
            r-=1
        max_vals_arr.append(m_val)
        ind+=1
    return max_vals_arr
    '''
print(Pali_Perm("cat taco"))
print(One_away("pale", "bake"))
print(String_Comp("abc"))
Rot_Matrix([[1, 2, 3, 4],[5, 6, 7, 8], [9,10,11,12], [13, 14, 15, 16]])
#print(zero_mat([[1,0,2],[4,5,6]]))
#print(string_rot("waterbottle","erbottlewat"))
#print(search_rotation([3,4,5,6,7,8,9,10,1,2], 10))
#print(fourSum([1,2],[-2,-1],[-1,2],[0,2]))
#print(max_window([1,3,-1,-3,5,3,6,7]
#,3))
