# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        '''
        Algorithm:
        - The concept of steps ahead pointer
        '''
        if head.next == None:
            return None
        slow = head
        ahead = head
        for i in range(n):
            ahead = ahead.next
        prev = slow
        if ahead == None:
            print("hi")
            head = head.next
            return head
        while ahead != None:
            prev = slow
            slow = slow.next
            ahead = ahead.next
        slow = prev
        
        if slow.next == None:
            slow = None
        else:
            slow.next = slow.next.next
        
        return head