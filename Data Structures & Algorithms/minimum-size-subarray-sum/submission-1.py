class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_window, l, curr_sum = float('inf'), 0, 0
        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                min_window = min(min_window, r - l + 1)
                curr_sum -= nums[l]
                l += 1
        return 0 if min_window == float('inf') else min_window