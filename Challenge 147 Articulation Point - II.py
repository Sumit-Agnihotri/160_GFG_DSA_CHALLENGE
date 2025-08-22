V = 5
edges = [[0, 1], [1, 4], [4, 3], [4, 2], [2, 3]]

class Solution:
    def articulationPoints(self, V, edges):
        g = [[] for _ in range(V)]
        for u, v in edges:
            g[u].append(v)
            g[v].append(u)
        tin, low, vis = [-1] * V, [-1] * V, [0] * V
        timer, ans = [0], set()
        
        def dfs(u, p):
            vis[u] = 1
            tin[u] = low[u] = timer[0]
            timer[0] += 1
            c = 0
            for v in g[u]:
                if v == p: continue
                if vis[v]:
                    low[u] = min(low[u], tin[v])
                else:
                    dfs(v, u)
                    low[u] = min(low[u], low[v])
                    if low[v] >= tin[u] and p != -1:
                        ans.add(u)
                    c += 1
                if p == -1 and c > 1:
                    ans.add(u)
        for i in range(V):                                                                          
            if not vis[i]:
                dfs(i, -1)
        return sorted(ans) if ans else [-1]

s = Solution()
print(s.articulationPoints(V, edges)) # Output: [1, 4]