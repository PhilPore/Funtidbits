#look at this again: https://leetcode.com/problems/4sum/
#can use
# [1,0,-1,0,-2,2]
#  target: 0
#for example

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        #pairs = {}
        #ret_arr = []
        def ksum(nums,target, k):
            sol = []
            if (len(nums) == 0 or nums[0]*k > target or nums[-1]*k < target):
                return sol
            if k == 2:
                return twosum(sol,nums,target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for subset in ksum(nums[i+1:],target-nums[i],k-1):
                        sol.append([nums[i]]+subset)
            return sol
        
        def twosum(sol,nums,target):
            res = []
            lo = 0
            hi = len(nums)-1
            while lo < hi:
                cur = nums[lo]+nums[hi]
                if cur < target or (lo > 0 and nums[lo] == nums[lo-1]):
                    lo+=1
                elif cur > target or (hi < len(nums)-1 and nums[hi] == nums[hi+1]):
                    hi-=1
                else:
                    res.append([nums[lo],nums[hi]])
                    lo+=1
                    hi-=1
            return res
                    
        
        
        
        nums.sort()
        return ksum(nums,target,4)
