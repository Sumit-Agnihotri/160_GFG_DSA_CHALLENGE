s = "1[b]"

class Solution:
    def decoded_string(self, s):
        stack = []
        for c in s:
            if c != "]":
                stack.append(c)
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k) * substr)
        return "".join(stack)

s = Solution()
print(s.decoded_string("1[b]"))  # Output: "b"