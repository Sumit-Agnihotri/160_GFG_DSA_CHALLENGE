class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# Helper function to build tree from list input
def build_tree(nodes):
    if not nodes or nodes[0] == 'N':
        return None
    root = Node(nodes[0])
    queue = [root]
    i = 1
    while queue and i < len(nodes):
        curr = queue.pop(0)
        if i < len(nodes) and nodes[i] != 'N':
            curr.left = Node(nodes[i])
            queue.append(curr.left)
        i += 1
        if i < len(nodes) and nodes[i] != 'N':
            curr.right = Node(nodes[i])
            queue.append(curr.right)
        i += 1
    return root

root_list = [1, 2, 3, 'N', 'N', 4]
root = build_tree(root_list)

class Solution:
    def mirror(self, root):
        if root is None:
            return
        self.mirror(root.left)
        self.mirror(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
        
# Function to print the tree in level order for verification
def print_tree(root):
    if not root:
        return "N"
    queue = [root]
    result = []
    while queue:
        curr = queue.pop(0)
        if curr:
            result.append(curr.data)
            queue.append(curr.left)
            queue.append(curr.right)
        else:
            result.append('N')
    # Remove trailing 'N's
    while result and result[-1] == 'N':
        result.pop()
    return result

s = Solution()
s.mirror(root)    
# Print the mirrored tree in level order
print(print_tree(root))