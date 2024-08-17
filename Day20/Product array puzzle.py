#User function Template for python3

class Solution:
    def productExceptSelf(self, nums):
        #code here
        prod = 1
        flag = 0
        for i in nums:
            if i != 0:
                prod *= i
            else:
                flag += 1
        if flag > 1:
            for k in range(len(nums)):
                nums[k] = 0
            return nums
        if flag == 1:
            for j in range(len(nums)):
                if nums[j] == 0:
                    nums[j] = prod
                else:
                    nums[j] = 0
        else:
            for j in range(len(nums)):
                nums[j] = prod // nums[j]
        return nums