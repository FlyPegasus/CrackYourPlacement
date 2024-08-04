# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        temp = head
        c = 0
        stk = []
        while temp != None:
            stk.append(temp.val)
            temp = temp.next
        counter = 0
        i = 0
        temp = head
        while temp != None:
            if counter % 2 == 0:
                temp.val = stk[i]
                
                i += 1
            else:
                temp.val = stk.pop()
            counter += 1
            temp = temp.next