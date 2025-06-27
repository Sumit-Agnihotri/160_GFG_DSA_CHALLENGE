# Node definition
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BST construction: [2, 1, 3]
root = Node(2)
root.left = Node(1)
root.right = Node(3)
k = 2

# Solution class
class Solution:
    def kthSmallest(self, root, K):
        self.k = K
        self.res = -1

        def inorder(node):
            if not node or self.res != -1:
                return
            inorder(node.left)
            self.k -= 1
            if self.k == 0:
                self.res = node.data
                return
            inorder(node.right)

        inorder(root)
        return self.res

# Run
sol = Solution()
print("K-th Smallest Element:", sol.kthSmallest(root, k))