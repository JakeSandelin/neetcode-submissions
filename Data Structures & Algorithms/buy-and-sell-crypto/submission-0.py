class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = prices[0]
        res = 0
        
        for sell in prices:
            res = max(res, sell-buy)
            if buy > sell:
                buy = sell
        
        return res
