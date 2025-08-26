n = 4
adjList = [[1, 2], [0, 2], [0, 1, 3], [2]]

class Node:
    def __init__(self, val):
        self.val, self.neighbors = val, []

class Solution:
    def cloneGraph(self, node):
        old_to_new = {}
        def dfs(n):
            if n in old_to_new: return old_to_new[n]
            copy = Node(n.val)
            old_to_new[n] = copy
            copy.neighbors = [dfs(nei) for nei in n.neighbors]
            return copy
        return dfs(node) if node else None

# Build original graph
nodes = [Node(i) for i in range(n)]
for i in range(n):
    nodes[i].neighbors = [nodes[j] for j in adjList[i]]

# Clone and print
cloned = Solution().cloneGraph(nodes[0])
def print_graph(node, seen=set()):
    if node in seen: return []
    seen.add(node)
    return [[nei.val for nei in node.neighbors]] + sum((print_graph(nei, seen) for nei in node.neighbors), [])
print(print_graph(cloned))