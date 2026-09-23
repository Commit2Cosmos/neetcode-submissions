class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        left, right = 0, len(nums)-1

        if nums[left] < nums[right]:
            return nums[left]

        mid = right//2

        while left < right:
            if nums[right] > nums[mid]:
                right = mid
            else:
                left = mid+1

            mid = (right+left)//2

        return nums[mid]