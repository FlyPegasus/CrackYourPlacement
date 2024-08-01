# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode()
        temp1 = l1
        temp2 = l2
        temp3 = ans
        temp = 0
        while temp1 != None and temp2 != None:
            t = temp1.val + temp2.val + temp
            temp = 0
            if t > 9:
                temp = t//10
                temp3.next = ListNode(t%10)
            else:
                temp3.next = ListNode(t)
            temp3 = temp3.next
            temp1 = temp1.next
            temp2 = temp2.next
        while temp1 != None:
            t = temp1.val + temp
            temp = 0
            if t > 9:
                temp = t//10
                temp3.next = ListNode(t%10)
            else:
                temp3.next = ListNode(t)
            temp3 = temp3.next
            temp1 = temp1.next
        while temp2 != None:
            t = temp2.val + temp
            temp = 0
            if t > 9:
                temp = t//10
                temp3.next = ListNode(t%10)
            else:
                temp3.next = ListNode(t)
            temp3 = temp3.next
            temp2 = temp2.next
        if temp == 1:
            temp3.next = ListNode(1)
        return ans.next