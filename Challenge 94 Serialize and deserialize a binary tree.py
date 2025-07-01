class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Construct the binary tree: [1, 2, 3]
root = Node(1)
root.left = Node(2)
root.right = Node(3)

class Solution:
    def serialize(self, root):
        def dfs(node):
            if not node: return ["#"]
            return [str(node.data)] + dfs(node.left) + dfs(node.right)
        return dfs(root)

    def deSerialize(self, arr):
        def dfs():
            val = next(vals)
            if val == "#": return None
            node = Node(int(val))
            node.left = dfs()
            node.right = dfs()
            return node
        vals = iter(arr)
        return dfs()

def inorder(root):
    return inorder(root.left) + [root.data] + inorder(root.right) if root else []

s = Solution()
serialized = s.serialize(root)
deserialized = s.deSerialize(serialized)

print("Serialized:", serialized)
print("Inorder of Deserialized Tree:", inorder(deserialized))  # [2, 1, 3]