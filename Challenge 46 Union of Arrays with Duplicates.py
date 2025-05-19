a = [1, 2, 3, 4, 5]
b = [1, 2, 3]

class Solution:    
    def findUnion(self, a, b):
        set1 = set()
        for i in range(len(a)):
            set1.add(a[i])
        for i in range(len(b)):
            set1.add(b[i])
        res = []
        for it in set1:
            res.append(it)
        return len(res)

s = Solution()
print(s.findUnion(a, b)) # Output: 5