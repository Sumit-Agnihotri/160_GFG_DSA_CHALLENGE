# Define the TreeNode class
class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Helper function to build BST from level order list
def build_bst_from_level_order(arr):
    if not arr or arr[0] == 'N':
        return None
    root = TreeNode(arr[0])
    queue = [root]
    i = 1
    while queue and i < len(arr):
        current = queue.pop(0)
        if i < len(arr) and arr[i] != 'N':
            current.left = TreeNode(arr[i])
            queue.append(current.left)
        i += 1
        if i < len(arr) and arr[i] != 'N':
            current.right = TreeNode(arr[i])
            queue.append(current.right)
        i += 1
    return root

root_list = [7, 3, 8, 2, 4, 'N', 9]
target = 12
root = build_bst_from_level_order(root_list)

class Solution:
    def findTarget(self, root, target):
        def inorder(node):
            return inorder(node.left)+[node.data]+inorder(node.right) if node else []
        vals = inorder(root)
        l, r = 0, len(vals)-1
        while l < r:
            s = vals[l] + vals[r]
            if s == target:
                return True
            if s < target:
                l += 1
            else:
                r -= 1
        return False

s = Solution()
print(s.findTarget(root, target))  # Output: True