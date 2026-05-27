class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        '''
        for buy in range(0,len(prices)):
            for sell in range(buy+1,len(prices)):
                max_profit = max(max_profit,prices[sell]-prices[buy])
        return max_profit
        
        buy = 0
        sell = len(prices)-1
        while buy < sell:
            current_profit = prices[sell]-prices[buy]
            max_profit = max(max_profit,current_profit)
            if current_profit < max_profit:
                sell -=1
            elif current_profit > max_profit:
                buy += 1
            else:
                buy += 1
                sell += 1
        return max_profit
        '''
        maxP=0
        minbuy = prices[0]
        for sell in prices:
            maxP = max(maxP,sell-minbuy)
            minbuy = min(minbuy,sell)
        return maxP
        