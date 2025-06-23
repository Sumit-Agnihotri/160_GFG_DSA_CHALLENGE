# Define the Node class for the binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Helper function to build tree from list (level order)
def buildTree(arr):
    if not arr or arr[0] == 'N':
        return None
    root = Node(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        curr = queue.pop(0)
        if i < len(arr) and arr[i] != 'N':
            curr.left = Node(arr[i])
            queue.append(curr.left)
        i += 1
        if i < len(arr) and arr[i] != 'N':
            curr.right = Node(arr[i])
            queue.append(curr.right)
        i += 1
    return root

arr = [1, 2, 3, 4, 5, 6, 7, 'N', 'N', 8, 9, 'N', 'N', 'N', 'N']
root = buildTree(arr)

class Solution:
    def boundaryTraversal(self, root):
        if not root: return []
        res = [root.data] if not self.isLeaf(root) else []
        
        def leftBoundary(node):
            while node:
                if not self.isLeaf(node): res.append(node.data)
                node = node.left if node.left else node.right
        
        def leaves(node):
            if node and self.isLeaf(node):
                res.append(node.data)
            elif node:
                leaves(node.left)
                leaves(node.right)
        def rightBoundary(node):
            stack = []
            while node:
                if not self.isLeaf(node): stack.append(node.data)
                node = node.right if node.right else node.left
            res.extend(stack[::-1])
            
        leftBoundary(root.left)
        leaves(root)
        rightBoundary(root.right)
        return res
    def isLeaf(self, node):
        return not node.left and not node.right

s = Solution()
print(s.boundaryTraversal(root))  # Output: [1, 2, 4, 8, 9, 5, 6, 3, 7]