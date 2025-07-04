import heapq

class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None
    def __lt__(self, other): return self.data < other.data

class Solution:
    def merge_k_lists(self, arr):
        h = [node for node in arr if node]
        heapq.heapify(h)
        dummy = Node(-1)
        tail = dummy
        while h:
            node = heapq.heappop(h)
            tail.next = node
            tail = tail.next
            if node.next: heapq.heappush(h, node.next)
        return dummy.next

s = Solution()# Helper function to create a linked list from a list of values
def create_linked_list(lst):
    if not lst:
        return None
    head = Node(lst[0])
    current = head
    for val in lst[1:]:
        current.next = Node(val)
        current = current.next
    return head

# Example usage:
arr = [
    create_linked_list([1, 2, 3]),
    create_linked_list([4, 5]),
    create_linked_list([5, 6]),
    create_linked_list([7, 8])
]

s = Solution()
result = s.merge_k_lists(arr)

# Print merged linked list
while result:
    print(result.data, end=" ")
    result = result.next
print()