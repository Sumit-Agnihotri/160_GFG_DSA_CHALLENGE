prices = [10, 22, 5, 75, 65, 80]

class Solution:
    def maxProfit(self, prices):
        n = len(prices)
        left = [0] * n
        right = [0] * n
        
        minp = prices[0]
        for i in range(1, n):
            minp = min(minp, prices[i])
            left[i] = max(left[i-1], prices[i] - minp)
        
        maxp = prices[-1]
        for i in range(n-2, -1, -1):
            maxp = max(maxp, prices[i])
            right[i] = max(right[i+1], maxp - prices[i])
            
        return max(left[i] + right[i] for i in range(n))

s = Solution()
print(s.maxProfit(prices))  # Output: 87