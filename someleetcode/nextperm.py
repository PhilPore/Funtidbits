#https://leetcode.com/problems/next-permutation/

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        r = len(nums)-2
        while r >= 0 and nums[r+1] <= nums[r]:
            r-=1
        
        r_2 = len(nums)-1
        
        if r >=0:
            while nums[r_2] <= nums[r]:
                r_2-=1
            nums[r],nums[r_2] = nums[r_2],nums[r]
        
        nums[r+1:] = nums[r+1:][::-1]
            
