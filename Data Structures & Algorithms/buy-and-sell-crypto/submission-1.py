class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        #for i in range(len(prices)):
        #    for j in range(i+1,len(prices)):
        #        profit = max(profit,prices[j]-prices[i])
        #return profit
        max_profit = 0
        min_buy = prices[0]
        for index,val in enumerate(prices):
            max_profit = max(max_profit,val-min_buy)
            min_buy = min(min_buy,val)
        return max_profit


        