class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''stk = dict()
        for i in nums:
            if i in stk:
                return i
            else:
                stk[i] = 1'''
        # another solution
        nums.sort()
        temp = 9999999
        for i in nums:
            if i == temp:
                return i
            temp = i