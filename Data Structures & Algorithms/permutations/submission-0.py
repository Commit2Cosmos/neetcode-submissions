class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        
        def recur(to_ignore_idx: List[int], curr: List[int]):
            if len(curr) == len(nums):
                res.append(curr.copy())
                return

            for i in range(len(nums)):
                if i in to_ignore_idx:
                    continue
                curr.append(nums[i])
                to_ignore_idx.append(i)
                recur(to_ignore_idx, curr)
                curr.pop()
                to_ignore_idx.pop()
        
        recur([], [])

        return res