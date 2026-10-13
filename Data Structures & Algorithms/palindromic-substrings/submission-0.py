class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0

        for center in range(len(s)):
            # add single char
            res += 1

            # find odd-count palindromes
            left, right = center-1, center+1
            while left >= 0 and right < len(s) and s[right] == s[left]:
                left -= 1
                right += 1
                res += 1

            # find even-count palindromes
            left, right = center, center+1
            while left >= 0 and right < len(s) and s[right] == s[left]:
                left -= 1
                right += 1
                res += 1

        return res