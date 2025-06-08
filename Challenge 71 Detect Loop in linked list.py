class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def detectLoop(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True  # Loop detected
        return False  # No loop

# Function to create linked list and insert loop
def createLinkedList(values, pos):
    if not values:
        return None

    head = Node(values[0])
    current = head
    loop_node = None

    for i in range(1, len(values)):
        current.next = Node(values[i])
        current = current.next
        if i + 1 == pos:  # 1-based indexing
            loop_node = current

    if pos == 1:
        loop_node = head

    if pos != 0:
        current.next = loop_node  # Create loop

    return head

# Input
values = [1, 3, 4]
pos = 2

# Create linked list with loop
head = createLinkedList(values, pos)

# Detect loop
sol = Solution()
has_loop = sol.detectLoop(head)
print("True" if has_loop else "False")  # Output: True