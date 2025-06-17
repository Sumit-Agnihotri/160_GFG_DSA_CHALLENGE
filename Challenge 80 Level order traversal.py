class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Construct the binary tree: 
#     1
#    / \
#   2   3
root = Node(1)
root.left = Node(2)
root.right = Node(3)

from collections import deque
class Solution:
    def levelOrder(self, root):
        if root is None:
            return[]
        res = []
        q = deque()
        currLevel = 0
        q.append(root)
        while q:
            len_q = len(q)
            res.append([])
            for i in range(len_q):
                node = q.popleft()
                res[currLevel].append(node.data)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
            currLevel += 1
        return res

s = Solution()
print(s.levelOrder(root)) # Output: [[1], [2, 3]]