class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        i,j = 0,len(prices) - 1
        previous_price,max_price = 1000,0
        for i in range(len(prices)):
            previous_price = min(previous_price,prices[i])
            max_price = max(prices[i] - previous_price,max_price)
        return max_price
            

        