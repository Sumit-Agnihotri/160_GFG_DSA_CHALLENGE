V = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 0], [2, 3]]

class Solution:
    def isCycle(self, V, edges):
        g = [[] for _ in range(V)]
        for u, v in edges:
            g[u].append(v)
        vis = [0] * V
        def dfs(u):
            if vis[u] == 1: return True
            if vis[u] == 2: return False
            vis[u] = 1
            for v in g[u]:
                if dfs(v): return True
            vis[u] = 2
            return False
        return any(dfs(i) for i in range(V) if vis[i] == 0)

s = Solution()
print(s.isCycle(V, edges))  # Output: True