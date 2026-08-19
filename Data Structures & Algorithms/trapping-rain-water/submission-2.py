class Solution:
    def trap(self, height: List[int]) -> int:
        left,right,sum = 0,0,0
        maxL = [0] * len(height)
        maxR = [0] * len(height)
        for i in range(1,len(height)):
            left = max(left,height[i-1])
            right = max(right,height[-i])
            maxL[i] = left
            maxR[-i-1] = right
        for i in range(len(height)):
            if min(maxL[i],maxR[i]) - height[i]>0:
                sum += min(maxL[i],maxR[i]) - height[i]
        return sum