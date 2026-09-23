class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # (num - target) -> index
        s = {}

        for i in range(len(nums)):
            if nums[i] in s.keys():
                return [s[nums[i]], i]
            
            s[target - nums[i]] = i