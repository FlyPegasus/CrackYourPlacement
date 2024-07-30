# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        # preorder traversal
        # leaf node : both children null
        flag = 0
        
        if root == None:
            return False
        s = root.val
        def trav(root):
            nonlocal s
            if root == None:
                return
            if root.left == None and root.right == None:
                if s == targetSum:
                    nonlocal flag
                    flag = 1
            if root.left != None:
                s += root.left.val
            trav(root.left)
            if root.left != None:
                s -= root.left.val
            if root.right != None:
                s += root.right.val
            trav(root.right)
            if root.right != None:
                s -= root.right.val
            
        trav(root)
        if flag == 1:
            return True
        return False