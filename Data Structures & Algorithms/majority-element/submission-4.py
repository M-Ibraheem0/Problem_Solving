from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        val = nums[0]
        count = 0
        for num in nums:
            val = num if count == 0 else val
            count += 1 if num == val else -1
        return val