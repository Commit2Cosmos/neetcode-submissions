class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        braces_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            print(stack)
            if char in braces_map.values():
                stack.append(char)
            else:
                if len(stack) == 0:
                    return False
                last_char = stack.pop()
                if braces_map[char] != last_char:
                    return False

        if len(stack) > 0:
            return False

        return True