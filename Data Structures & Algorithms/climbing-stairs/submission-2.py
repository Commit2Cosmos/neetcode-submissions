class Solution:
    def climbStairs(self, n: int) -> int:

        memo = {}
        
        def recur(step):
            if step == n:
                return 1
            if step > n:
                return 0

            if step not in memo:
                memo[step] = recur(step+1) + recur(step+2)
            
            return memo[step]

        
        return recur(0)