"""
Given an array of distinct integers candidates and a target integer target, 
return a list of all unique combinations of candidates where the chosen numbers sum to target. 
You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. 
Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations 
 sum up to target is less than 150 combinations for the given input.

"""

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        set_list = []
        if len(candidates) == 0:
            return set_list
        def get_sets(cur_sum,index,path): #dfs, go down as far as we can for each guy
            if cur_sum < 0:
                return
            if cur_sum == 0:
                set_list.append(list(path))
            #by using the same index we allow repeats, however this means
            #that no candidate can go back. Which logically makes sense given
            #that if you were to find the path earlier you wouldnt need to do it again.
            for i in range(index,len(candidates)):
                get_sets(cur_sum-candidates[i],i,path+[candidates[i]])
                
            
            
        
        get_sets(target,0,[])
        return set_list
        """
        previous get sets function. Pretty bad ik
        def get_sets(arr, targ):
            if sum(arr) == target:
                t_arr = sorted(arr)
                for i in set_list:
                    if sorted(i) == t_arr:
                        return
                set_list.append(list(arr))
                return
            if sum(arr) < target:
                for i in candidates:
                    arr.append(i)
                    #(arr)
                    get_sets(arr,targ)
                    arr.pop()
        
        get_sets([],target)
        return set_list
        
        
        """    