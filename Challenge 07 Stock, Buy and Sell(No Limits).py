prices = [100, 180, 260, 310, 40, 535, 695]

from typing import List


class Solution:
    def maximumProfit(self, price_list) -> int:
        res = 0
        
        for i in range(1, len(price_list)):
            if price_list[i] > price_list[i - 1]:
                res += price_list[i] - price_list[i - 1]
        
        return res
    
s = Solution()
print(s.maximumProfit(prices))  # Output: 865