adj = [[2, 3, 1], [0], [0, 4], [0], [2]]

from collections import deque

class Solution:
    def bfs(self, adj):
        vis = [0] * len(adj)
        q = deque([0])
        res = []
        vis[0] = 1
        while q:
            u = q.popleft()
            res.append(u)
            for v in adj[u]:
                if not vis[v]:
                    vis[v] = 1
                    q.append(v)
        return res

s = Solution()
print(s.bfs(adj))  # Output: [0, 2, 3, 1, 4]