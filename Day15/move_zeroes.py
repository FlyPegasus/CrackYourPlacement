class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i = 0
        j = 0
        
        while i < len(nums) and j < len(nums):
            while j < len(nums) and nums[j] == 0:
                j += 1
            if nums[i] == 0 and j < len(nums) and j > i:
                nums[i] = nums[j]
                nums[j] = 0
                continue
            i += 1
            j = i