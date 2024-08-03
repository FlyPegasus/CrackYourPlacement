# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stk1 = []
        stk2 = []
        temp1 = l1
        temp2 = l2
        while temp1 != None and temp2 != None:
            stk1.append(temp1.val)
            stk2.append(temp2.val)
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1 != None:
            stk1.append(temp1.val)
            temp1 = temp1.next
        while temp2 != None:
            stk2.append(temp2.val)
            temp2 = temp2.next
        temp = 0
        ans = ListNode()
        tr = ans
        while len(stk1) > 0 and len(stk2) > 0:
            ans = ListNode()
            t = stk1.pop() + stk2.pop() + temp
            temp = 0
            temp = t // 10
            tr.val = t%10
            ans.next = tr
            tr = ans
        while len(stk1) > 0:
            ans = ListNode()
            t = stk1.pop() + temp
            temp = 0
            temp = t // 10
            tr.val = t%10
            ans.next = tr
            tr = ans
        while len(stk2) > 0:
            ans = ListNode()
            t = stk2.pop() + temp
            temp = 0
            temp = t // 10
            tr.val = t%10
            ans.next = tr
            tr = ans
        if temp == 1:
            ans = ListNode()
            tr.val = 1
            ans.next = tr
            tr = ans
        return ans.next