from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int)
        count,currSum = 0,0
        for num in nums:
            currSum += num
            if currSum == k:
                count += 1
            diff = currSum - k
            count += prefix_count[diff]
            prefix_count[currSum] += 1
        return count