# Creating the linked list: 1 -> 2 -> 3 -> 4 -> 5
class ListNode:
    def __init__(self, val=0, next_node=None):
        self.val = val
        self.next = next_node

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))

class Solution:
    def reverseList(self, node):
        curr = node
        prev = None
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        node = prev
        return node
        
        # Call the reverseList method and print the reversed list
sol = Solution()
reversed_head = sol.reverseList(head)
        
        # Print the reversed linked list
curr = reversed_head
while curr:
    print(curr.val, end=" ")
    curr = curr.next
print()