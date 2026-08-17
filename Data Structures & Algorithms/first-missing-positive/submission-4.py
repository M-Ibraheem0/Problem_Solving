class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i < len(nums):
            if nums[i] <=0 or nums[i] > len(nums) or nums[nums[i]-1]==nums[i]:
                i += 1
                continue
            index = nums[i] - 1
            nums[i],nums[index] = nums[index],nums[i]
        val = 1
        for i in range(len(nums)):
            if nums[i] != val:
                return val
            val += 1
        return val