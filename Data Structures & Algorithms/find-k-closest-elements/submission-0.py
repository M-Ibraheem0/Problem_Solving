class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr):
            return arr
        l,diff,prev_val,prev_arr = 0,10001,10001,[]
        for r in range(len(arr)):
            diff += abs(x - arr[r])
            if len(prev_arr) >=k and diff < prev_val:
                prev_arr = arr[l : r + 1]
            if r - l + 1 >= k:
                prev_val = diff
                if len(prev_arr) == 0:
                    prev_arr = arr[l:r+1]
                diff -= abs(x-arr[l])
                l += 1
        return prev_arr

