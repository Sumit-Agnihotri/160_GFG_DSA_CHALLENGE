# Define the Node class for the binary tree
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Helper function to build a binary tree from a list (level order)
def buildTree(lst):
    if not lst or lst[0] == 'N':
        return None
    root = Node(lst[0])
    queue = [root]
    i = 1
    while queue and i < len(lst):
        curr = queue.pop(0)
        if i < len(lst) and lst[i] != 'N':
            curr.left = Node(lst[i])
            queue.append(curr.left)
        i += 1
        if i < len(lst) and lst[i] != 'N':
            curr.right = Node(lst[i])
            queue.append(curr.right)
        i += 1
    return root

# Input list (use 'N' as a string for None/null nodes)
lst = [2, 1, 3, 'N', 'N', 'N', 5]
root = buildTree(lst)

class Solution:
    def isBST(self, root):
        prev = [None]
        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if prev[0] is not None and node.data <= prev[0]:
                return False
            prev[0] = node.data
            return inorder(node.right)
        return inorder(root)

# Example usage:
sol = Solution()
print(sol.isBST(root))  # Output: True