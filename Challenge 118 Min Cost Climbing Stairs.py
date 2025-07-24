cost = [10, 15, 20]

class Solution:
    def min_cost_climbing_stairs(self, cost):
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])

s = Solution()
print(s.min_cost_climbing_stairs(cost))  # Output: 15