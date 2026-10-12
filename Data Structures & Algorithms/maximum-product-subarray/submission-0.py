class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        
        max_end, min_end, best = nums[0], nums[0], nums[0]

        for i in range(1, len(nums)):
            x = nums[i]

            candidates = (x, x*max_end, x*min_end)
            max_end = max(candidates)
            min_end = min(candidates)

            best = max(max_end, best)

        return best