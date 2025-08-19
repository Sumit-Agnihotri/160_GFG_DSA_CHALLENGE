V = 4
E = 3
edges = [[3, 0], [1, 0], [2, 0]]

from collections import deque

class Solution:
    def topoSort(self, V, edges):
        g = [[] for _ in range(V)]
        indeg = [0]*V
        for u, v in edges:
            g[u].append(v)
            indeg[v] += 1
        q = deque([i for i in range(V) if not indeg[i]])
        res = []
        while q:
            u = q.popleft()
            res.append(u)
            for v in g[u]:
                indeg[v] -= 1
                if indeg[v] == 0:
                    q.append(v)
        return res

s = Solution()
print(s.topoSort(V, edges))  # Output: [1, 2, 3, 0]