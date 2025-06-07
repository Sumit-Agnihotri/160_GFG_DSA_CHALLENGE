class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.random = None

def buildLinkedList(arr):
    if not arr:
        return None
    nodes = [Node(val[0]) for val in arr]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    for i in range(len(arr)):
        if arr[i][1] != 'NULL':
            nodes[i].random = nodes[arr[i][1]]
    return nodes[0]

def printList(head):
    result = []
    while head:
        rand = head.random.data if head.random else 'NULL'
        result.append([head.data, rand])
        head = head.next
    print(result)

class Solution:
    def cloneLinkedList(self, head):
        if not head:
            return None
        curr = head
        while curr:
            newNode = Node(curr.data)
            newNode.next = curr.next
            curr.next = newNode
            curr = curr.next.next
        curr = head
        while curr:
            if curr.random:
                curr.next.random = curr.random.next
            curr = curr.next.next
        cloneHead = head.next
        curr = head
        cloneCurr = cloneHead
        while cloneCurr.next:
            curr.next = curr.next.next
            cloneCurr.next = cloneCurr.next.next
            curr = curr.next
            cloneCurr = cloneCurr.next
        curr.next = None
        cloneCurr.next = None
        return cloneHead

# Input: [value, random_index or 'NULL']
head_input = [[1, 3], [3, 3], [5, 'NULL'], [9, 3]]
head = buildLinkedList(head_input)

sol = Solution()
cloned_head = sol.cloneLinkedList(head)

printList(cloned_head)