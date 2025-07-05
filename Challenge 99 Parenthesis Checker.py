s = "[{()}]"

class Solution:
    def is_balanced(self, s):
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        for char in s:
            if char in bracket_map.values():
                stack.append(char)
            elif char in bracket_map:
                if not stack or stack[-1] != bracket_map[char]:
                    return False
                stack.pop()
        return not stack

sol = Solution()
print(sol.is_balanced(s))  # Output: True