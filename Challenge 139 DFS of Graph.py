adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

class Solution:
    def dfs(self, adj):
        vis, res = [0] * len(adj), []
        def go(u):
            vis[u] = 1
            res.append(u)
            for v in adj[u]:
                if not vis[v]:
                    go(v)
        go(0)
        return res

s = Solution()
print(s.dfs(adj))  # Output: [0, 2, 4, 3, 1]