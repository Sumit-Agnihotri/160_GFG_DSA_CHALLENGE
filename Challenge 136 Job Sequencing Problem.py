deadline = [4, 1, 1, 1]
profit = [20, 10, 40, 30]

class Solution:
    def jobSequencing(self, deadline, profit):
        n = len(deadline)
        jobs = sorted(zip(profit, deadline), key = lambda x :-x [0])
        max_deadline = max(deadline)
        parent = list(range(max_deadline + 1))
        
        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x
        
        count = total_profit = 0
        for p, d in jobs:
            slot = find(d)
            if slot > 0:
                count += 1
                total_profit += p
                parent[slot] = find(slot - 1)
        return [count, total_profit]

s = Solution()
print(s.jobSequencing(deadline, profit))  # Output: [2, 60]