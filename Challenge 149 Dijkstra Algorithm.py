V = 3
edges = [[0, 1, 1], [1, 2, 3], [0, 2, 6]]
src = 2

import heapq
class Solution:
    def dijkstra(self, V, edges, src):
        graph = [[] for _ in range(V)]
        for u, v, w in edges:
            graph[u].append((v, w))
            graph[v].append((u, w))
        dist = [float("inf")] * V
        dist[src] = 0
        pq = [(0, src)]
        
        while pq:
            d, u = heapq.heappop(pq)
            if d > dist[u]:
                continue
            for v, w in graph[u]:
                if dist[v] > d + w:
                    dist[v] = d + w
                    heapq.heappush(pq, (dist[v], v))
        return dist

s = Solution()
print(s.dijkstra(V, edges, src)) # Output: [4, 3, 0]