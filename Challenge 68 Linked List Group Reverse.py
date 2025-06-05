# Definition for singly-linked list node
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Helper function to create a linked list from a list
def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

# Helper function to print a linked list
def print_linked_list(head):
    while head:
        print(head.val, end=" -> " if head.next else "")
        head = head.next
    print()

# Your provided solution (no changes)
class Solution:
    def reverseKGroup(self, head, k):
        curr = head
        newHead = None
        tail = None
        while curr:
            groupHead = curr
            count = 0
            prev = None
            while curr and count < k:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
                count += 1
            if newHead is None:
                newHead = prev
            if tail is not None:
                tail.next = prev
            tail = groupHead
        return newHead

# Input
arr = [1, 2, 2, 4, 5, 6, 7, 8]
k = 4
head = create_linked_list(arr)

# Solution call
sol = Solution()
new_head = sol.reverseKGroup(head, k)

# Output
print("Reversed in groups of", k, ":")
print_linked_list(new_head)