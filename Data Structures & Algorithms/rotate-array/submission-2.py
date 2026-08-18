class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums1 = nums.copy()
        if k > len(nums):
            k %= len(nums)
        nums2,nums3 = nums1[:len(nums)-k],nums1[len(nums)-k:]
        print(nums2,nums3)
        k = 0
        for i in range(len(nums3)):
            nums[k] = nums3[i]
            k += 1
        for i in range(len(nums2)):
            nums[k] = nums2[i]
            k += 1
        
        