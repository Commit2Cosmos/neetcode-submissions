class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        subsets = set()

        def recur(i, curr_set):
            subsets.add(tuple(curr_set))

            for j in range(i, len(nums)):
                curr_set.append(nums[j])
                recur(j+1, curr_set)
                curr_set.remove(nums[j])

        recur(0, [])

        return list(subsets)