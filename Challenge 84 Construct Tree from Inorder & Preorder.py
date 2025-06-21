inorder = [1, 6, 8, 7]
preorder = [1, 6, 7, 8]

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Solution:
    def buildTreeRec(self, l, h, preorder, mp, index):
        if l > h:
            return None
        value = preorder[index[0]]
        root = Node(value)
        index[0] += 1
        root.left = self.buildTreeRec(l, mp[value] - 1, preorder, mp, index)
        root.right = self.buildTreeRec(mp[value] + 1, h, preorder, mp, index)
        return root
    
    def buildTree(self, inorder, preorder):
        index = [0]
        n = len(inorder)
        mp = {}
        for i in range(n):
            mp[inorder[i]] = i
        root = self.buildTreeRec(0, n - 1, preorder, mp, index)
        return root

s = Solution()
root = s.buildTree(inorder, preorder) # Output : [8, 7, 6, 1]

# Postorder traversal to match the expected output
def postorder(root):
    return postorder(root.left) + postorder(root.right) + [root.data] if root else []

print(postorder(root))