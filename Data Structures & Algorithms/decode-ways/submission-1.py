class Solution:
    def numDecodings(self, s: str) -> int:

        nums_set = set([i for i in range(1,27)])

        def recur(i, prev_char):
            key = (i, prev_char)
            if key in memo:
                return memo[key]

            if i == len(s) and (prev_char == "" or prev_char in nums_set):
                return 1

            if i >= len(s):
                return 0

            res = 0
            if prev_char:
                if int(prev_char+s[i]) in nums_set:
                    res += recur(i+1, "")

            elif int(s[i]) in nums_set:
                res += recur(i+1, "")
                res += recur(i+1, f"{s[i]}")

            memo[key] = res
            return memo[key]

        memo = {}

        return recur(0, "")