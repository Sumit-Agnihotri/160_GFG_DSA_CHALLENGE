prices = [7, 10, 1, 3, 6, 9, 2]

class Solution:
    def maximumProfit(self, prices):
        minSoFar = prices[0]
        res = 0
        
        for i in range(1,len(prices)):
            minSoFar = min(minSoFar, prices[i])
            
            res = max(res, prices[i] - minSoFar)
            
        return res

s = Solution()
print(s.maximumProfit(prices))