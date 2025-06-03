class Node:
	def __init__(self, data):
		self.data = data
		self.next = None

# Create linked list: 10 -> 20 -> 30 -> 40 -> 50
head = Node(10)
head.next = Node(20)
head.next.next = Node(30)
head.next.next.next = Node(40)
head.next.next.next.next = Node(50)

k = 4

class Solution:
    def rotate(self, head, k):
        if k == 0 or head is None:
            return head
        len = 1
        curr = head
        while curr.next is not None:
            len += 1
            curr = curr.next
        k = k % len
        if k == 0:
            return head
        curr.next = head
        curr = head
        for i in range(1, k):
            curr = curr.next
        head = curr.next
        curr.next = None
        return head

s = Solution()
rotated_head = s.rotate(head, k)
# Print the rotated linked list
curr = rotated_head
while curr is not None:
    print(curr.data, end=" -> ")
    curr = curr.next # Output: 450 -> 10 -> 20 -> 30 -> 40