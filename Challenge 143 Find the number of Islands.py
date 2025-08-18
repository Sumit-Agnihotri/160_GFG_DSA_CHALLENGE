g = [['L', 'L', 'W', 'W', 'W'], ['W', 'L', 'W', 'W', 'L'], ['L', 'W', 'W', 'L', 'L'], ['W', 'W', 'W', 'W', 'W'], ['L', 'W', 'L', 'L', 'W']]

class Solution:
    def numIslands(self, g):
        n,m = len(g),len(g[0])
        def dfs(i,j):
            if 0<=i<n and 0<=j<m and g[i][j] == "L":
                g[i][j] = "W"
                for x in [-1, 0, 1]:
                    for y in [-1, 0, 1]:
                        if x or y: dfs(i+x, j+y)
        c = 0
        for i in range(n):
            for j in range(m):
                if g[i][j] == "L":
                    dfs(i,j)
                    c += 1
        return c

s = Solution()
print(s.numIslands(g))  # Output: 4