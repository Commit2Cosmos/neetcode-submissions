class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        result = set()
        nums.sort()

        for i in range(len(nums)-2):
            target = -nums[i]

            left, right = i+1, len(nums)-1

            while left < right:
                if nums[left] + nums[right] < target:
                    left += 1
                elif nums[left] + nums[right] > target:
                    right -= 1
                else:
                    result.add((nums[i], nums[left], nums[right]))
                    left += 1
                    right -= 1

        return list(result)