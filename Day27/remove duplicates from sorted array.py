class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        i = 0
        j = 0
        while i < len(nums) and j < len(nums):
            while j < len(nums) and nums[i] == nums[j]:
                j += 1
            if i + 1 < len(nums) and j < len(nums):
                i += 1
                nums[i] = nums[j]
        return i + 1