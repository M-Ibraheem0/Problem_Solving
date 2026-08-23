class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final_temp = [0] * len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                index = stack.pop()[0]
                final_temp[index] = i - index
            stack.append([i,temp])
        return final_temp