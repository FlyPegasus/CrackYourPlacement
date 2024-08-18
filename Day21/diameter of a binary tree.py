# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxDia = 0
        def maxDepth(root):
            if root == None:
                return -1
            l = maxDepth(root.left) + 1
            r = maxDepth(root.right) + 1
            nonlocal maxDia
            if r + l > maxDia:
                maxDia = r + l
            return max(r, l)
        maxDepth(root)
        return maxDia