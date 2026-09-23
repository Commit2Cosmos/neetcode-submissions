class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def recur(idx, curr_elements):
            res.append(curr_elements)
            for e in range(idx, len(nums)):
                recur(e+1, [*curr_elements, nums[e]])

        recur(0, [])
 
        return res