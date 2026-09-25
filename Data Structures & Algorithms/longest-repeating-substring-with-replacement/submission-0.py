class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        res = 1
        left = 0
        counts = {s[0]: 1}

        for right in range(1, len(s)):
            if s[right] not in counts:
                counts[s[right]] = 1
            else:
                counts[s[right]] += 1

            while (right-left+1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
            
            res = max(res, right-left+1)

        return res