a = [10, 20, 30, 50, 10, 70, 30]

class Solution:
    def maxOfMins(self, a):
        n = len(a)
        l, r, s = [-1] * n, [n] * n, []
        for i in range(n):
            while s and a[s[-1]] >= a[i]: s.pop()
            l[i] = s[-1] if s else -1
            s.append(i)
        s.clear()
        for i in range(n - 1, -1, -1):
            while s and a[s[-1]] >= a[i]: s.pop()
            r[i] = s[-1] if s else n
            s.append(i)
        res = [0] * (n + 1)
        for i in range(n): res[r[i] - l[i] - 1] = max(res[r[i] - l[i] - 1], a[i])
        for i in range(n - 1, 0, -1): res[i] = max(res[i], res[i + 1])
        return res[1:]

s = Solution()
print(s.maxOfMins(a))  # Output: [70, 30, 20, 10, 10, 10, 10]