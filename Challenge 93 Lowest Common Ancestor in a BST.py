input_list = ['5', '4', '6', '3', 'N', 'N', '7', 'N', 'N', 'N', '8']
n1 = 7
n2 = 8

from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Build tree from level-order input list
def buildTree(values):
    if not values or values[0] == 'N':
        return None

    root = Node(int(values[0]))
    q = deque([root])
    i = 1

    while q and i < len(values):
        curr = q.popleft()

        # Left child
        if values[i] != 'N':
            curr.left = Node(int(values[i]))
            q.append(curr.left)
        i += 1
        if i >= len(values): break

        # Right child
        if values[i] != 'N':
            curr.right = Node(int(values[i]))
            q.append(curr.right)
        i += 1

    return root

# LCA function
class Solution:
    def LCA(self, root, n1, n2):
        if root.data > max(n1, n2):
            return self.LCA(root.left, n1, n2)
        if root.data < min(n1, n2):
            return self.LCA(root.right, n1, n2)
        return root

# Build tree
root = buildTree(input_list)

# Find LCA
sol = Solution()
lca = sol.LCA(root, n1, n2)

# Print result
print(f"LCA of {n1} and {n2} is: {lca.data}")