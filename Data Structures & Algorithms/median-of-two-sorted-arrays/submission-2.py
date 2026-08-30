class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A,B = nums1,nums2
        if len(A) > len(B):
            A,B = B,A
        total = len(A) + len(B)
        half = (total + 1) // 2
        A_left,A_right = 0, len(A)
        while A_left <= A_right:
            mid = (A_left + A_right) // 2
            mid_2 = half - mid
            Aleft = A[mid - 1] if mid > 0 else float('-inf')
            Aright = A[mid] if mid < len(A) else float('inf')
            Bleft = B[mid_2 - 1] if mid_2 > 0 else float('-inf')
            Bright = B[mid_2] if mid_2 < len(B) else float('inf')
            if Aleft <= Bright and Bleft <= Aright:
                if (len(A) + len(B)) % 2 == 0:
                    return (max(Aleft,Bleft) + min(Aright,Bright)) / 2
                else:
                    return max(Aleft,Bleft)
            elif Aleft > Bright:
                A_right = mid - 1
            else:
                A_left = mid + 1
        