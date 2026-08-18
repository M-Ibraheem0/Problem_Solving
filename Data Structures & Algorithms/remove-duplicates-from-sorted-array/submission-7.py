class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        k = 1
        i,j = 1,2
        while i < len(nums) and j < len(nums):
            if nums[i] <= nums[i-1]:
                while j < len(nums) and (nums[j] <= nums[i] or nums[i-1] >= nums[j]):
                    j += 1
                if j < len(nums):
                    nums[i] = nums[j]
            i += 1
        print(nums)
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                k += 1
            else:
                break
        return k