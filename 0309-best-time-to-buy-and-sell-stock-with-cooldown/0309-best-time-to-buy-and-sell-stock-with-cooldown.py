class Solution(object):
    def maxProfit(self, prices):
        if not prices:
            return 0
        
        hold = -prices[0]   # buy చేసినట్టు
        sold = 0            # sell చేసినట్టు
        rest = 0            # nothing
        
        for i in range(1, len(prices)):
            prev_sold = sold
            
            sold = hold + prices[i]      # sell today
            hold = max(hold, rest - prices[i])  # buy or keep holding
            rest = max(rest, prev_sold)  # cooldown or stay
            
        return max(sold, rest)