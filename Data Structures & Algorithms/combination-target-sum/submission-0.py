class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []

        def recur(idx, part_sum, curr_elements):
            if part_sum > target:
                return

            elif part_sum == target:
                res.append(curr_elements)
                return

            for e in range(idx, len(nums)):
                recur(e, part_sum+nums[e], [*curr_elements, nums[e]])

        recur(0, 0, [])
 
        return res