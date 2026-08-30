class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        if k > len(nums):
            return -1
        left,right = max(nums),sum(nums)
        while(left <= right):
            mid = (left + right) // 2
            val,total = k - 1,mid
            for num in nums:
                if total - num < 0:
                    val -= 1
                    total = mid
                total -= num
            if val >= 0:
                right = mid - 1
            else:
                left = mid + 1
        return left