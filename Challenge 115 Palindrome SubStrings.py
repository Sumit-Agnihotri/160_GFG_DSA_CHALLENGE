s = "abaab"

class Solution:
    def count_ps(self, s):
        n=len(s)
        count=0
        def expand(l,r):
            nonlocal count
            while l>=0 and r<n and s[l] == s[r]:
                if r-l+1>=2:
                    count += 1
                l -=1
                r += 1
        
        for i in range(n):
            expand(i,i)
            expand(i,i+1)
        return count

sol = Solution()
print(sol.count_ps(s))  # Output: 3