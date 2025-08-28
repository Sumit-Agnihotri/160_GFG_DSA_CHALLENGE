V = 5
edges = [[1, 3, 2], [4, 3, -1], [2, 4, 1], [1, 2, 1], [0, 1, 5]]
src = 0

class Solution:
    def bellmanFord(self, V, edges, src):
        dist = [float("inf")] * V
        dist[src] = 0
        for _ in range(V-1):
            for u, v, w in edges:
                if dist[u] != float("inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        
        for u, v, w in edges:
            if dist[u] != float("inf") and dist[u] + w < dist[v]:
                return [-1]
                
        return [d if d != float("inf") else 10 ** 8 for d in dist]

s = Solution()
print(s.bellmanFord(V, edges, src)) # Output: [0, 5, 6, 6, 7]