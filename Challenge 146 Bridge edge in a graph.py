V = 4
edges = [[0, 1], [1, 2], [2, 3]]
c = 1
d = 2

class Solution:
    def isBridge(self, V, edges, c, d):
        g = [[] for _ in range(V)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        g[c].remove(d)
        g[d].remove(c)
        vis = [False] * V
        def dfs(u):
            vis[u] = True
            for v in g[u]:
                if not vis[v]:
                    dfs(v)
        dfs(c)
        return not vis[d]

s = Solution()
print(s.isBridge(V, edges, c, d))  # Output: True