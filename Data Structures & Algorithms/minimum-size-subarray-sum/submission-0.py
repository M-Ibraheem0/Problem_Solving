class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_window,l,sum = 100001,0,0
        for r in range(len(nums)):
            sum += nums[r]
            while sum >= target:
                min_window = min(min_window,r - l + 1)
                sum -= nums[l]
                l += 1
        return 0 if min_window == 100001 else min_window

