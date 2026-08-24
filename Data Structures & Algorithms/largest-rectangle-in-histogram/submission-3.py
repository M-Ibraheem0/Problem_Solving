class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        largest_rectangle,n = 0,len(heights)
        for i,height in enumerate(heights):
            real_idx = i
            while stack and height < stack[-1][0]:
                val,idx = stack.pop()
                largest_rectangle = max((real_idx - idx) * val,largest_rectangle)
                i = idx
            else:
                stack.append([height,i])
        for height,i in stack:
            largest_rectangle = max(largest_rectangle,(n - i) * height)
        return largest_rectangle