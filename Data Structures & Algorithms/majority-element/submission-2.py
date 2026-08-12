from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # return Counter(nums).most_common(1)[0][0]
        val = nums[0]
        count = 0
        for num in nums:
            count += 1 if num == val else -1
            if count == 0:
                val = num
                count += 1
        return val

