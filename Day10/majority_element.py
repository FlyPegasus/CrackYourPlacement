class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        stk = dict()
        for i in nums:
            if i in stk:
                stk[i] += 1
            else:
                stk[i] = 1
        minm = 0
        ans = -1
        for j in stk:
            if stk[j] > minm:
                ans = j
                minm = stk[j]
        return ans