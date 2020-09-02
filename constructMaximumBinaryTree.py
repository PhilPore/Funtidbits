#leetcode problem 654. Medium: Maximum Binary Tree. I
#t works! I did some edits though because in the problem its part of a class so I got peeved when I tried to do recursio and forgot the self.<method>. Don't be like me. Be smarter.
'''
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    / 
     2  0   
       \
        1

'''
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right
def constructMaximumBinaryTree(nums: List[int]) -> TreeNode:
        if len(nums) == 1:
            return TreeNode(nums[0])
        place = 0
        maxr = nums[0]
        for i in range(len(nums)):
            if nums[i] > maxr:
                maxr = nums[i]
                place = i
        #print(maxr)
        #set max to head of the tree/subtree
        trnode = TreeNode(maxr)
        print("{} {}".format(maxr, place))
        #recurse
        if place != 0: #make sure something exists on the left
            trnode.left= constructMaximumBinaryTree(nums[:place])
        if place != len(nums)-1: #make sure something exists on the right
            trnode.right= constructMaximumBinaryTree(nums[place+1:])
        return trnode
   
   
