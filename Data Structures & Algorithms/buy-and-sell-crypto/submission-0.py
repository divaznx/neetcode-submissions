class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = [0]
        for buy in range(len(prices)):
            for sell in range(buy+1,len(prices)):
                max_profit.append(prices[sell] - prices[buy])
        return max(max_profit)