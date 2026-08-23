class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        final_temp = [0] * len(temperatures)
        stack = []
        for i,temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                index = stack.pop()
                final_temp[index] = i - index
            stack.append(i)
        return final_temp