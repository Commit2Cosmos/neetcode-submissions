class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        min_jump = 1
        for i in range(len(nums)-2, -1, -1):
            print(f"{i}: {min_jump}")
            if nums[i] == 0 or nums[i] < min_jump:
                min_jump += 1
            else:
                min_jump = 1

        if nums[0] < min_jump:
            return False
        return True
