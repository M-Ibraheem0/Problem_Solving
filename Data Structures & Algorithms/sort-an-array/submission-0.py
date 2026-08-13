class Solution:
    def merge(self,left,right):
        result = []
        i,j = 0,0
        while i<len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        while i < len(left):
            result.append(left[i])
            i += 1
        while j< len(right):
            result.append(right[j])
            j+=1
        return result
    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) <=1:
            return nums
        mid = len(nums) // 2
        left = self.sortArray(nums[0:mid])
        right = self.sortArray(nums[mid:len(nums)])
        return self.merge(left,right)