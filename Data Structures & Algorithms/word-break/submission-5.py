class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        wordDict = set(wordDict)

        if s in wordDict:
            return True
        
        def recur(i, memo):
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            for j in range(i+1, len(s)+1):
                if s[i:j] in wordDict and recur(j, memo):
                        memo[i] = True
                        return True

            memo[i] = False
            return False
        
        return recur(0, {})