class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Creating first linked list: 5 -> 10 -> 15 -> 40
head1 = Node(5)
head1.next = Node(10)
head1.next.next = Node(15)
head1.next.next.next = Node(40)

# Creating second linked list: 2 -> 3 -> 20
head2 = Node(2)
head2.next = Node(3)
head2.next.next = Node(20)

class Solution:
    def sortedMerge(self,head1, head2):
        dummy = Node(-1)
        curr = dummy
        while head1 and head2:
            if head1.data <= head2.data:
                curr.next = head1
                head1 = head1.next
            else:
                curr.next = head2
                head2 = head2.next
            curr = curr.next
        if head1:
            curr.next = head1
        else:
            curr.next = head2
            
        return dummy.next

s = Solution()
# Merging the two linked lists
merged_head = s.sortedMerge(head1, head2)
# Function to print the linked list
def printList(node):
    while node:
        print(node.data, end=" -> ")
        node = node.next
    print("None")

# Printing the merged linked list
printList(merged_head)