class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        
        dp = [[0, 0] for _ in range(len(prices))]

        dp[0][1] = -prices[0]

        for i in range(1, len(prices)):
            # no share owned: either did nothing or sold a share
            dp[i][0] = max(dp[i-1][0], dp[i-1][1] + prices[i])

            if i >= 2:
                # share owned: either did nothing or bought a share
                dp[i][1] = max(dp[i-1][1], dp[i-2][0]-prices[i])

            else:
                # share owned: either did nothing or bought a share on first day
                dp[i][1] = max(dp[i-1][1], -prices[i])

        # result = max profit with no shares left (cz dp[-1][1] >= dp[-1][0])
        return dp[-1][0]