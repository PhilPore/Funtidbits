# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        
        """
        :type root: TreeNode
        :rtype: bool
        """
        def isValidRec(root, min_val, max_val):
            ''' Other method.
                has a range the root value must be in. Adjust the range as we go left/right
                initially the range values (-inf,inf), later goes on to be
                (min, max)
                left: (min_value,current root value)
                right(current root value, max value). 
                The numbers adjust
            '''
            if not root:
                return True
            #print("--")
            #print("{} {} {}".format(min_val,max_val,root.val))
            if root.val <= min_val or root.val >= max_val:
                return False
            return isValidRec(root.left,min_val,root.val) and isValidRec(root.right,root.val,max_val)
        
        return isValidRec(root,float("-inf"),float("inf"))
        
        
        """
        A working solsution. GOod job brain
        arr = []
        def inord(root):
            if root.left:
                inord(root.left)
            arr.append(root.val)
            
            if root.right:
                inord(root.right)
        inord(root)
        #print(arr)
        
        for i in range(len(arr)-1):
            if arr[i+1] <= arr[i]:
                return False
        return True
        """
        
        """
        a solution that doesnt really work.
        if root == None:
            return True
        if root.left == None and root.right == None:
            return True
        
        if (root.left and root.left.val >= root.val) or (root.right and root.right.val <= root.val):
            return False
        
        return self.isValidBST(root.left) and self.isValidBST(root.right)
        """ 
        