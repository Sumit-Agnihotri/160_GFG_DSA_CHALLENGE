class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# Input: num1 = 4 -> 5
num1 = Node(4)
num1.next = Node(5)

# Input: num2 = 3 -> 4 -> 5
num2 = Node(3)
num2.next = Node(4)
num2.next.next = Node(5)

class Solution:
    def trimLeadingZeros(self, head):
        while head and head.data == 0:
            head = head.next
        return head
        
    def length(self, head):
        len = 0
        while head:
            head = head.next
            len += 1
        return len
    
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
        
    def addTwoLists(self, num1, num2):
        num1 = self.trimLeadingZeros(num1)
        num2 = self.trimLeadingZeros(num2)
        len1 = self.length(num1)
        len2 = self.length(num2)
        
        if len1 < len2:
            return self.addTwoLists(num2, num1)
            
        num1 = self.reverse(num1)
        num2 = self.reverse(num2)
        res = num1
        
        carry = 0
        while num2 or carry != 0:
            num1.data += carry
            if num2 is not None:
                num1.data += num2.data
                num2 = num2.next
            carry = num1.data // 10
            num1.data = num1.data % 10
            if num1.next is None and carry != 0:
                num1.next = Node(0)
            num1 = num1.next
        return self.reverse(res)
    
s = Solution()
def printList(head):
    while head:
        print(head.data, end=" -> ")
        head = head.next
    print("None")
result = s.addTwoLists(num1, num2)
printList(result)  # Output: 3 -> 9 -> 0 -> None