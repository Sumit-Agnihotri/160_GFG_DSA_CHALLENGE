root = [10, 2, 10, 20, 1, None, -25, None, None, None, None, 3, 4]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = self.right = None

def buildTree(i, arr):
    if i >= len(arr) or arr[i] is None:
        return None
    node = Node(arr[i])
    node.left = buildTree(2 * i + 1, arr)
    node.right = buildTree(2 * i + 2, arr)
    return node

class Solution:
    def findMaxSum(self, root):
        def dfs(node):
            if not node: return 0
            l = max(0, dfs(node.left))
            r = max(0, dfs(node.right))
            self.res = max(self.res, l + r + node.data)
            return max(l, r) + node.data
        self.res = float('-inf')
        dfs(root)
        return self.res

root_node = buildTree(0, root)
print(Solution().findMaxSum(root_node))  # Output: 42