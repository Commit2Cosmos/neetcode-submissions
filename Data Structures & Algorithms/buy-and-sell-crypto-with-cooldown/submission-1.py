class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        def recur(idx_buy, idx_sell):
            if idx_sell >= len(prices) or idx_buy >= len(prices):
                return 0
            
            if memo[idx_buy][idx_sell] is not None:
                return memo[idx_buy][idx_sell]

            memo[idx_buy][idx_sell] = max(prices[idx_sell]-prices[idx_buy] + recur(idx_sell+2, idx_sell+3), recur(idx_buy, idx_sell+1), recur(idx_buy+1, idx_sell+1))
            return memo[idx_buy][idx_sell]

        memo = [[None] * len(prices) for _ in range(len(prices))]
        return recur(0,1)