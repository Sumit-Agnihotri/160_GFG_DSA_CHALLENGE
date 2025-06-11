
class Solution:
    def removeLoop(self, head):
        if not head or not head.next:
            return
        slow = head
        fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
            
        else:
            return
        
        slow = head
        if slow == fast:
            while fast.next != slow:
                fast = fast.next
            fast.next = None
            return
        
        while slow.next != fast.next:
            slow = slow.next
            fast = fast.next
        fast.next = None

# Example usage:
# Assuming the linked list is defined as follows:
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next
# Creating a linked list with a loop for testing
head = ListNode(1)
head.next = ListNode(3)
head.next.next = ListNode(4)
head.next.next.next = head.next  # Creating a loop for testing

s = Solution()
s.removeLoop(head)

# Now we can call the removeLoop method
# to remove the loop from the linked list
# and print the modified linked list
def print_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")
print_list(head)