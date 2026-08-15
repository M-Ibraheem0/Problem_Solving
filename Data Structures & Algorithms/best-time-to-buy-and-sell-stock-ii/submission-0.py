class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sum = 0
        for i in range(len(prices) - 1):
            if prices[i] > prices[i+1]:
                continue
            sum += prices[i+1] - prices[i]
        return sum