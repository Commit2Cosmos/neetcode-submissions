class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        letter_index = lambda char: ord(char) - ord('a')

        def word_2_lst(word):
            word_lst = [0] * 26
            for l in word:
                word_lst[letter_index(l)] += 1
            return word_lst

        anagrams = {}

        for s in strs:
            s_as_lst = tuple(word_2_lst(s))
            if s_as_lst in anagrams:
                anagrams[s_as_lst].append(s)
            else:
                anagrams[s_as_lst] = [s]

        return list(anagrams.values())