# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        num = 0
        r = 0
        def trav(root):
            if root == None:
                return
            trav(root.next)
            nonlocal num
            nonlocal r
            num += 2**r*root.val
            r += 1
        trav(head)
        return num