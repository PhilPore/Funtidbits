# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        
        """
        #better solution. It creates temp variaboles that have the tree subsets
        """
        ex:
                         1
                       2   5
                      3 4    6
                    
                    flatten_left at the very bottom would first return 3, flatten_right would have 4
                    prune the left and right on the current node to be none
                    make a sub tree starting at 2, then make 2's right = to flatten left 
                    now sub tree is: 2 R-> 3
                    go down sub tree until right is None, then make Right = flatten_right
                    2 R-> 3 R-> 4

                    ^ covers left side. 
                    Right would return None for flatten left
                    6 for flatten right
                    temp tree 5, R-> flattne_left so 5-> None
                    eventually 5 R-> 6
                    bubble back to root, 1.
                    root's right = flatten left meaning 1 R-> 2 R-> 3 R-> 4
                    go down till right is None, then add flatten_right 5 R-> 6
                    we finally get 1 R-> 2 R-> 3 R-> 4 R-> 5 R-> 6

        """


        if root == None:
            return root
        flatten_left = self.flatten(root.left)
        root.left = None
        flatten_right = self.flatten(root.right)
        root.right = None
        root.right = flatten_left
        
        temp = root
        while temp.right:
            temp = temp.right
        temp.right = flatten_right
        return root
        
        """
        my solution. Uses more space than needed.
        #temp_T = root
        if root == None:
            return None
        #root.left = None
        node_arr = []
        def make_flat(node):
            if node != None:
                node_arr.append(node)
                make_flat(node.left)
                make_flat(node.right)
        make_flat(root)
        temp = root
        #temp.left = None
        
        
        for i in range(1,len(node_arr)):
            temp.right = node_arr[i]
            temp.left = None
            temp = temp.right
        #tr = root
        #for i in range(len(node_arr)):
            #print(tr.val)
            #tr = tr.right
            
            
        #print(node_arr)
            
            
        """