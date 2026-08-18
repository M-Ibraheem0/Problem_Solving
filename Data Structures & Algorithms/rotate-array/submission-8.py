class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == len(nums):
            return None
        if k > len(nums):
            k %= len(nums)
        i,j = 0,len(nums) - 1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        print(nums)
        i,j = 0,k - 1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
        print(nums)
        i,j = k,len(nums)-1
        while i < j:
            nums[i],nums[j] = nums[j],nums[i]
            i += 1
            j -= 1
