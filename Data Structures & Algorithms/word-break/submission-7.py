class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)
        
        def recur(i):
            if i == len(s):
                return True

            if memo[i] is not None:
                return memo[i]

            res = False
            
            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict:
                    res = res or recur(j)

            memo[i] = res
            return memo[i]

        memo = [None]*len(s)

        return recur(0)
