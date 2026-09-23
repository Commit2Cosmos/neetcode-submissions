class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        
        def recur(curr_step, memo):

            if curr_step >= len(cost):
                return 0

            if curr_step not in memo:
                memo[curr_step] = cost[curr_step] + min(recur(curr_step+1, memo), recur(curr_step+2, memo))

            return memo[curr_step]

        memo = {}

        return min(recur(0, memo), recur(1, memo))