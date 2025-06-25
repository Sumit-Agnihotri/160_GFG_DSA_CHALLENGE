class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

k = 7
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(3)
root.left.right = Node(7)
root.right.right = Node(18)

class Solution:
    def sumKRec(self, root, k, res, prefixSumMap, currSum):
        if root is None:
            return
        
        # Update current sum
        currSum += root.data

        # Count paths ending at current node with sum k
        res[0] += prefixSumMap.get(currSum - k, 0)

        # Update map with current sum
        prefixSumMap[currSum] = prefixSumMap.get(currSum, 0) + 1

        # Recurse
        self.sumKRec(root.left, k, res, prefixSumMap, currSum)
        self.sumKRec(root.right, k, res, prefixSumMap, currSum)

        # Backtrack
        prefixSumMap[currSum] -= 1

    def sumK(self, root, k):
        res = [0]
        prefixSumMap = {0: 1}  # 🔥 FIXED LINE: start with sum 0 count = 1
        self.sumKRec(root, k, res, prefixSumMap, 0)
        return res[0]

# Run it
s = Solution()
print(s.sumK(root, k)) # Output: 3