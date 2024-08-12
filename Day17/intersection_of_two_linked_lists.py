# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        stk = dict()
        temp = headA
        t2 = headB
        while temp != None and t2 != None:
            if temp in stk:
                return temp
            stk[temp] = 1
            if t2 in stk:
                return t2
            stk[t2] = 1
            temp = temp.next
            t2 = t2.next
        while temp != None:
            if temp in stk:
                return temp
            temp = temp.next
        while t2 != None:
            if t2 in stk:
                return t2
            t2 = t2.next
        return None