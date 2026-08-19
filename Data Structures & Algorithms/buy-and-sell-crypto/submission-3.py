class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        previous_price,max_price = 101,0
        for i in range(len(prices)):
            previous_price = min(previous_price,prices[i])
            max_price = max(prices[i] - previous_price,max_price)
        return max_price