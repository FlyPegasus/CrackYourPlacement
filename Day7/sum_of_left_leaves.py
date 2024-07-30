# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        s = 0
        def trav(root):
            if root == None:
                return
            if root.left != None:
                if root.left.left == None and root.left.right == None:
                    nonlocal s
                    s += root.left.val
            trav(root.left)
            trav(root.right)
        trav(root)
        return s