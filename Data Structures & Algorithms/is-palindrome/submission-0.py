class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_cleaned = ''.join(ch for ch in s if ch.isalnum()).casefold().lower()
        left, right = 0, len(s_cleaned)-1

        while left < right:
            if s_cleaned[left] != s_cleaned[right]:
                return False
            
            left +=1
            right -=1

        return True