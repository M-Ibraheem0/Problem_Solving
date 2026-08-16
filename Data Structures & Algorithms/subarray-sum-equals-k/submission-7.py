from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        count,currSum = 0,0
        prefix_count[0] = 1
        for num in nums:
            currSum += num
            count += prefix_count[currSum - k]
            prefix_count[currSum] += 1
        return count
