# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head
        if head == None or head.next == None:
            return False
        fast = fast.next
        while fast.next != None and fast.next.next != None:
            if slow == fast:
                return True
            slow = slow.next
            fast = fast.next.next
        return False