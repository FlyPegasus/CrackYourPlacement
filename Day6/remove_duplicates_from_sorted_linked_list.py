# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head
        curr = head
        while temp != None:
            if temp.val != curr.val:
                curr.next = temp
                curr = curr.next
            temp = temp.next
        if curr != None:
            curr.next = None
        return head