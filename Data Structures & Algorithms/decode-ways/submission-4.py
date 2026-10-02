class Solution:
    def numDecodings(self, s: str) -> int:

        nums_set = set([f"{i}" for i in range(1,27)])

        prev_char = ""

        n = len(s) + 1
        dp = [0] * n
        dp[0] = 1

        for i in range(1, n):
            if s[i-1] in nums_set:
                dp[i] += dp[i-1]

            if i >= 2 and s[i-2:i] in nums_set:
                dp[i] += dp[i-2]
                

        return dp[-1]