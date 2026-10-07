class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        
        def recur(i, j):
            if i >= len(word1):
                return len(word2)-j

            if j >= len(word2):
                return len(word1)-i

            if (i,j) in memo:
                return memo[(i,j)]

            if word1[i] == word2[j]:
                memo[(i,j)] = recur(i+1, j+1)
                return memo[(i,j)]

            # delete, insert, replace

            memo[(i,j)] = 1+min(recur(i+1, j), recur(i+1, j+1), recur(i, j+1))
            return memo[(i,j)]

        memo = {}

        return recur(0, 0)