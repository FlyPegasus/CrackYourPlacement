class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        # three cases
        '''
        ///
        // /
        / //
         ///
        '''
        # first sorting the array
        nums.sort()
        # case 1
        prod = nums[0] * nums[1] * nums[2]
        temp = nums[0] * nums[1] * nums[-1]
        if temp > prod:
            prod = temp
        temp = nums[0] * nums[-2] * nums[-1]
        if temp > prod:
            prod = temp
        temp = nums[-3] * nums[-2] * nums[-1]
        if temp > prod:
            prod = temp
        return prod