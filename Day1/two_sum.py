class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        ''' Brute Force
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        
            Better
        stk = dict()
        for i in range(len(nums)):
            if target - nums[i] in stk:
                return [stk[target - nums[i]], i]
            else:
                stk[nums[i]] = i
        '''
        #Optimal
        nums.sort()
        # two pointers approach
        i = 0
        j = len(nums) - 1
        while i < j:
            if nums[i] + nums[j] == target:
                return [i, j]
            elif nums[i] + nums[j] < target:
                i += 1
            else:
                j -= 1