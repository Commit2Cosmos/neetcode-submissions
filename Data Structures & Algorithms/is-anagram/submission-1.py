class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        letter_index = lambda char: ord(char) - ord('a')

        s_map = [0] * 26

        for s_letter in s:
            s_map[letter_index(s_letter)] += 1

        for t_letter in t:
            s_map[letter_index(t_letter)] -= 1

        if any(s_map):
            return False

        return True
