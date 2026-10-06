class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        
        hashmap = {}

        for i in range(len(s)):
            if s[i] in hashmap:
                hashmap[s[i]] += 1
            else:
                hashmap[s[i]] = 1
        
        curr_set = set()
        res = []
        point = -1

        for i in range(len(s)):

            curr_set.add(s[i])
            hashmap[s[i]] -= 1

            if hashmap[s[i]] == 0:
                curr_set.remove(s[i])

            if len(curr_set) == 0:
                res.append(i-point)
                point = i

        return res