class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        def recur(p1, p2):
            if p1 >= len(text1) or p2 >= len(text2):
                return 0

            if memo[p1][p2]:
                return memo[p1][p2]

            if text1[p1] == text2[p2]:
                memo[p1][p2] = 1 + recur(p1+1, p2+1)
                return memo[p1][p2]

            memo[p1][p2] = max(recur(p1+1, p2), recur(p1, p2+1))
            return memo[p1][p2]

        memo = [[None]*len(text2) for _ in range(len(text1))]

        return recur(0, 0)