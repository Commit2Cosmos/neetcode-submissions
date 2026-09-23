class Solution:
    def climbStairs(self, n: int) -> int:
        
        def recur(step, memo):
            if step == n:
                return 1
            if step > n:
                return 0

            if step not in memo:
                memo[step] = recur(step+1, memo) + recur(step+2, memo)
            
            return memo[step]

        memo = {}
        return recur(0, memo)