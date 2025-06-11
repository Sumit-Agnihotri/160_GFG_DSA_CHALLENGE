class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def findFirstNode(self, head):
        slow = head
        fast = head

        # Step 1: Detect loop using Floyd’s algorithm
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None  # No loop

        # Step 2: Move slow to head, keep fast at meeting point
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next

        return slow  # First node of the loop

# Function to create a linked list and add loop at given position
def createLinkedList(values, pos):
    if not values:
        return None

    head = Node(values[0])
    current = head
    loop_node = None

    if pos == 1:
        loop_node = head

    for i in range(1, len(values)):
        current.next = Node(values[i])
        current = current.next
        if i + 1 == pos:
            loop_node = current

    if pos != 0:
        current.next = loop_node  # Create the loop

    return head

# Example Usage
values = [1, 2, 3, 4, 5]
pos = 3  # Loop starts at node with value 3

head = createLinkedList(values, pos)
sol = Solution()

first_node = sol.findFirstNode(head)
if first_node:
    print(f"✅ First node of loop is: {first_node.data}")
else:
    print("❌ No loop detected")