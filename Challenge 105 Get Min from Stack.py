q = 7
queries = [[1, 2], [1, 3], [3], [2], [4], [1, 1], [4]]

class Solution:

    def __init__(self):
        self.s = []
        self.mins = []
        
    def push(self, x):
        self.s.append(x)
        self.mins.append(x if not self.mins else min(x, self.mins[-1]))

    def pop(self):
        if self.s: self.mins.pop(); return self.s.pop()

    def peek(self):
        return self.s[-1] if self.s else -1

    def get_min(self):
        return self.mins[-1] if self.mins else -1

s = Solution()
for q in queries:
    if q[0] == 1:
        s.push(q[1])
    elif q[0] == 2:
        s.pop()
    elif q[0] == 3:
        print(s.peek())
    elif q[0] == 4:
        print(s.get_min())
    else:
        print("Invalid query")