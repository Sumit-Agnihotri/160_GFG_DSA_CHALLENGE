root = [12, 8, 18, 5, 11]

class Solution:
    def height(self, root):
        if root is None:
            return -1
        leftHeight = self.height(root.left)
        rightHeight = self.height(root.right)
        return max(leftHeight, rightHeight) + 1

s = Solution()
def build_tree(values):
    if not values:
        return None
    mid = len(values) // 2
    node = TreeNode(values[mid])
    node.left = build_tree(values[:mid])
    node.right = build_tree(values[mid + 1:])
    return node
class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
tree_root = build_tree(root)
height = s.height(tree_root)
print("Height of the binary tree is:", height)