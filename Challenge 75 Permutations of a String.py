s = "ABC"

class Solution:
    def permutations(self, i, n, res, cnt, perm):
        if i == n:
            res.append(perm)
            return
        for ch, count in cnt.items():
            if count == 0:
                continue
            cnt[ch] -= 1
            self.permutations(i + 1, n, res, cnt, perm + ch)
            cnt[ch] += 1
            
    def findPermutation(self, s):
        n = len(s)
        cnt = {}
        res = []
        for ch in s:
            cnt[ch] = cnt.get(ch, 0) + 1
        self.permutations(0, n, res, cnt, "")
        return res

s = Solution()
print(s.findPermutation(s))  # Output: ['ABC', 'ACB', 'BAC', 'BCA', 'CAB', 'CBA']