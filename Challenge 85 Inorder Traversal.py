class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Constructing the binary tree:
#         1
#        / \
#       2   3
#      / \
#     4   5
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

class Solution:
    def inOrder(self,root):
        res = []
        curr = root
        while curr:
            if curr.left is None:
                res.append(curr.data)
                curr = curr.right
            else:
                predecessor = curr.left
                while predecessor.right and predecessor.right != curr:
                    predecessor = predecessor.right
                if predecessor.right is None:
                    predecessor.right = curr
                    curr = curr.left
                else:
                    predecessor.right = None
                    res.append(curr.data)
                    curr = curr.right
        return res

s = Solution()
print(s.inOrder(root))  # Output: [4, 2, 5, 1, 3]