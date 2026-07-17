class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        '''min_price = prices[0]
        max_profit = 0
        for price in prices:
            min_price = min(price,min_price)
            current = price - min_price
            max_profit = max(max_profit,current)

        return max_profit'''

        profit = 0
        n = len(prices)
        for i in range(n):
            for j in range(i+1,n):
                current = prices[j]-prices[i]
                profit = max(profit,current)

        return profit