gas = [4, 5, 7, 4]
cost= [6, 6, 3, 5]

class Solution:
    def startStation(self, gas, cost):
        if sum(gas) < sum(cost): return -1
        tank = start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
        return start

s = Solution()
print(s.startStation(gas, cost))  # Output: 2