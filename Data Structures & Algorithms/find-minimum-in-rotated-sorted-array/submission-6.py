class Solution:
    def findMin(self, nums: List[int]) -> int:
        left,right = 0,len(nums) - 1
        lowest = float('inf')
        while left <= right:
            mid = (left + right) // 2
            lowest = min(lowest,nums[mid])
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid + 1
        return lowest