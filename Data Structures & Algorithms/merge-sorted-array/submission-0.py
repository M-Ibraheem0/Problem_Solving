class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums3 = nums1.copy()
        for i in range(m + n):
            nums1[i] = 0
        left,right,k = 0,0,0
        while left < m and right < n:
            if nums3[left] <= nums2[right]:
                nums1[k] = nums3[left]
                left += 1
                k += 1
            else:
                nums1[k] = nums2[right]
                right += 1
                k += 1
        while left < m:
            nums1[k] = nums3[left]
            left += 1
            k += 1
        while right< n:
            nums1[k] = nums2[right]
            right += 1
            k += 1
        