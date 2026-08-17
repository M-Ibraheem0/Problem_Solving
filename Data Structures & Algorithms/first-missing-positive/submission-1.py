class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        seen = set(nums)
        val = 1
        while val in seen:
            val += 1
        return val