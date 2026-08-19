class Solution:
    def maxArea(self, heights: List[int]) -> int:
        container = 0
        i,j = 0,len(heights) - 1
        while i<j:
            max_water = (j - i) * min(heights[i],heights[j])
            print(max_water)
            container = max(container,max_water)
            if heights[i] < heights[j]:
                i += 1
            else:
                j -= 1
        return container