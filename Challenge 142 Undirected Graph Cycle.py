V = 4
E = 4
edges = [[0, 1], [0, 2], [1, 2], [2, 3]]

class Solution:
    def isCycle(self, V, edges):
        parent = list(range(V))
        
        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]

        def union(x, y):
            px, py = find(x), find(y)
            if px == py:
                return True
            parent[px] = py
            return False
        
        for u, v in edges:
            if union(u, v):
                return True
        return False

s = Solution()
print(s.isCycle(V, edges))  # Output: True