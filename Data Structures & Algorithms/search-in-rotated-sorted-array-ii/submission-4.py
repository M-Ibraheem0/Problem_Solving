class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        left,right = 0,len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target or nums[left] == target or nums[right] == target:
                return True
            elif nums[mid] < nums[right]:
                if target > nums[mid] and target < nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            elif nums[mid] > nums[right]:
                if target > nums[mid] or target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1
            else:
                left += 1
        return  False