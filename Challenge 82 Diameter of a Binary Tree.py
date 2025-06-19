class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Construct the binary tree: [1, 2, 3]
root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)

class Solution:
    def diameterRec(self, root, res):
        if root is None:
            return 0
        lHeight = self.diameterRec(root.left, res)
        rHeight = self.diameterRec(root.right, res)
        res[0] = max(res[0], lHeight + rHeight)
        return 1 + max(lHeight, rHeight)
    def diameter(self, root):
        res = [0]
        self.diameterRec(root, res)
        return res[0]

s = Solution()
print(s.diameter(root))  # Output: 2