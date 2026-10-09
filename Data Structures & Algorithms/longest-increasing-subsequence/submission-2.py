class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        def recur(i, prev_idx):
            if i == len(nums):
                return 0

            if memo[i][prev_idx] is not None:
                return memo[i][prev_idx]

            res = recur(i+1, prev_idx)

            if prev_idx == 0 or nums[i] > nums[prev_idx-1]:
                res = max(res, 1 + recur(i+1, i+1))

            memo[i][prev_idx] = res
            
            return memo[i][prev_idx]

        memo = [[None] * (len(nums)+1) for _ in range(len(nums))]

        return recur(0, 0)