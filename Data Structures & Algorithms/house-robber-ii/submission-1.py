class Solution:
    def rob(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]

        def recur(i, arr, memo):
            if i >= len(arr):
                return 0

            if i+2 not in memo:
                memo[i+2] = recur(i+2, arr, memo)

            if i+3 not in memo:
                memo[i+3] = recur(i+3, arr, memo)

            return arr[i] + max(memo[i+2], memo[i+3])

        memo_1 = {}
        memo_2 = {}
        return max(recur(0, nums[:-1], memo_1), recur(1, nums[:-1], memo_1), recur(0, nums[1:], memo_2), recur(1, nums[1:], memo_2))