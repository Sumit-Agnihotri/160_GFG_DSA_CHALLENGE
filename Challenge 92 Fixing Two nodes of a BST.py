from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

class Solution:
    def correctBST(self, root):
        self.first = self.second = self.prev = None

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if self.prev and node.data < self.prev.data:
                if not self.first:
                    self.first = self.prev
                self.second = node
            self.prev = node
            inorder(node.right)

        inorder(root)
        if self.first and self.second:
            self.first.data, self.second.data = self.second.data, self.first.data
        return root

def printLevelOrder(root):
    if not root:
        return
    q = deque([root])
    result = []
    while q:
        node = q.popleft()
        result.append(str(node.data))
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    print(', '.join(result))

root = Node(10)
root.left = Node(5)
root.right = Node(8)
root.left.left = Node(2)
root.left.right = Node(20)

# 🚀 Fix the BST
sol = Solution()
fixed_root = sol.correctBST(root)
printLevelOrder(fixed_root)