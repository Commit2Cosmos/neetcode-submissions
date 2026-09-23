class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0

        if len(s) == 1:
            return 1

        seen = set()
        res = 1

        left = 0
        for right in range(0, len(s)):
            if s[right] in seen:
                while left < right and s[left] != s[right]:
                    seen.remove(s[left])
                    left += 1
                left += 1
            else:
                seen.add(s[right])
                res = max(res, right-left+1)

        return res