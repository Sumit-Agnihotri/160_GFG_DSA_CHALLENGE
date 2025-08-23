n = 5
houses = [[0, 7], [0, 9], [20, 7], [30, 7], [40, 70]]

class Solution:
    def minCost(self, houses):
        n = len(houses)
        min_dist = [float("inf")] * n
        visited = [0] * n
        min_dist[0] = 0
        res = 0
        
        for _ in range(n):
            u = -1
            for i in range(n):
                if not visited[i] and (u == -1 or min_dist[i] < min_dist[u]):
                    u = i
            visited[u] = 1
            res += min_dist[u]
            
            for v in range(n):
                if not visited[v]:
                    d = abs(houses[u][0] - houses[v][0]) + abs(houses[u][1] - houses[v][1])
                    if d < min_dist[v]:
                        min_dist[v] = d
                        
        return res

s = Solution()
print(s.minCost(houses))  # Output: 105