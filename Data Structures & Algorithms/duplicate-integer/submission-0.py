class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) in (0, 1):
            return False

        nums_set = set(nums)
        
        if len(nums) == len(nums_set):
            return False

        return True