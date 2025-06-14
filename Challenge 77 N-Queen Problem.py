n = 1

class Solution:
    def nQueen(self, n):
        def isSafe(perm, row, col):
            for c in range(col):
                if abs(perm[c] - row) == abs(c - col):
                    return False
            return True
            
        def solve(col, perm, used):
            if col == n:
                return [perm[:]]
            res = []
            for row in range(1, n + 1):
                if row not in used and isSafe(perm, row, col):
                    if isSafe(perm, row, col):
                        perm.append(row)
                        used.add(row)
                        res += solve(col + 1, perm, used)
                        perm.pop()
                        used.remove(row)
            return res
        return solve(0, [], set())

s = Solution()
print(s.nQueen(n)) # Output: [[1]]