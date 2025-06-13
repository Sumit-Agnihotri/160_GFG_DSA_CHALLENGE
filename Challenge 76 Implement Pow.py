b = 3.00000
e = 5

class Solution:
    def power(self, b: float, e: int) -> float:
        if e == 0:
            return 1
        if e < 0:
            return 1/self.power(b, -e)
            
        temp = self.power(b, e // 2)
        
        if e % 2 ==0:
            return temp * temp
        else:
            return temp * temp * b

s = Solution()
print(s.power(b, e))  # Output: 243.00000