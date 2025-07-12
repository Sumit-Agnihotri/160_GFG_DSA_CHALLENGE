arr = ["2", "3", "1", "*", "+", "9", "-"]

class Solution:
    def evaluate(self, A):
        s = []
        for x in A:
            if x in '+-*/':
                b, a = s.pop(), s.pop()
                s.append(a + b if x == '+' else a - b if x == '-' else a * b if x == '*' else int(a / b))
            else: s.append(int(x))
        return s[0]

s = Solution()
print(s.evaluate(arr))  # Output: -4