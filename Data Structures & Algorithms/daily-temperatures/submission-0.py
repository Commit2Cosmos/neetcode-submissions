class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # (idx, num)
        stack = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while len(stack) > 0 and temperatures[stack[-1]] < temperatures[i]:
                curr = stack.pop()
                res[curr] = i-curr

            stack.append(i)


        return res