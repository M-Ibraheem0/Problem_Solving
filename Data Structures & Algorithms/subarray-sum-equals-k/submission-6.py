from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        prefix_sum = [0] * len(nums)
        curr,count = 0,0
        for i in range(len(nums)):
            curr += nums[i]
            prefix_sum[i] = curr
        for i in range(len(nums)):
            if prefix_sum[i] == k:
                count += 1
            diff = prefix_sum[i] - k
            count += prefix_count[diff]
            prefix_count[prefix_sum[i]] += 1
        return count
