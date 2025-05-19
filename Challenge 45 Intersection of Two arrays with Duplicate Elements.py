a = [1, 2, 1, 3, 1]
b = [3, 1, 3, 4, 1]

class Solution:
    def intersectionWithDuplicates(self, a, b):
        s = set(a)
        res = []
        for element in b:
            if element in s:
                res.append(element)
                s.remove(element)
        return res

s = Solution()
print(s.intersectionWithDuplicates(a, b)) # Output: [3, 1]