class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""

        for i in range(len(strs)):
            s = strs[i]
            l = len(s)
            res += str(l) + "`" + s

        print(res)
        return res

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []

        while i < len(s):
            curr = ""

            while s[i] != "`":
                curr += s[i]
                i += 1

            i += 1

            word_len = int(curr)
            curr = ""

            for _ in range(word_len):
                curr += s[i]
                i += 1
            
            res.append(curr)

        return res
