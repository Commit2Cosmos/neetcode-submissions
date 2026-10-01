class Solution:
    def trap(self, height: List[int]) -> int:
        if len(height) <= 2:
            return 0

        res = 0

        prefix = [0] * len(height)
        prefix[0] = height[0]

        for i in range(1, len(prefix)):
            prefix[i] = max(height[i], prefix[i-1])
        
        
        postfix = [0] * len(height)
        postfix[-1] = height[-1]

        for i in range(len(postfix)-2, -1, -1):
            postfix[i] = max(height[i], postfix[i+1])

        for i in range(1, len(height)-1):
            res += max(min(prefix[i], postfix[i])-height[i], 0)

        return res