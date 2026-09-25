class Solution:
    def rob(self, nums: List[int]) -> int:

        def recur(i, memo):
            if i >= len(nums):
                return 0

            if i+2 not in memo:
                memo[i+2] = recur(i+2 ,memo)

            if i+3 not in memo:
                memo[i+3] = recur(i+3 ,memo)

            return nums[i] + max(memo[i+2], memo[i+3])

        memo = {}
        return max(recur(0, memo), recur(1, memo))