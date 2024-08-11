# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        if list1 == None and list2 == None:
            return None
        temp = head
        t1 = list1
        t2 = list2
        prev = temp
        while t1 != None and t2 != None:
            if t1.val < t2.val:
                temp.val = t1.val
                t1 = t1.next
            else:
                temp.val = t2.val
                t2 = t2.next
            v = ListNode()
            prev = temp
            temp.next = v
            temp = v
        while t1 != None:
            temp.val = t1.val
            t1 = t1.next
            v = ListNode()
            prev = temp
            temp.next = v
            temp = v
        s = temp
        while t2 != None:
            temp.val = t2.val
            t2 = t2.next
            f = ListNode()
            prev = temp
            temp.next = f
            temp = f
        prev.next = None
        return head