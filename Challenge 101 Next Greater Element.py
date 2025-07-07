arr = [1, 3, 2, 4]

class Solution:
    def nextLargerElement(self, arr):
        n, res, stack = len(arr), [-1] * len(arr), []
        for i in range(n - 1, -1, -1):
            while stack and stack[-1] <= arr[i] :stack.pop()
            if stack: res[i] = stack[-1]
            stack.append(arr[i])
        return res

s = Solution()
print(s.nextLargerElement(arr))  # Output: [3, 4, 4, -1]