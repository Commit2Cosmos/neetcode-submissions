class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        
        def recur(i, j):
            if j == len(t):
                return 1

            if i == len(s):
                return 0

            if memo[i][j] is not None:
                return memo[i][j]

            if s[i] == t[j]:
                memo[i][j] = recur(i+1, j+1) + recur(i+1, j)
                return memo[i][j]

            memo[i][j] = recur(i+1, j)
            return memo[i][j]

        memo = [[None] * len(t) for _ in range(len(s))]

        return recur(0, 0)

            