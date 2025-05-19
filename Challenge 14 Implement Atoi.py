s = "-123"

class Solution:
    def myAtoi(self, s):
        sign = 1
        res = 0
        idx = 0
        
        while idx < len(s) and s[idx] == " ":
            idx += 1
            
        if idx < len(s) and (s[idx] == "-" or s[idx] == "+"):
            if s[idx] == "-":
                sign = -1
            idx += 1
            
        while idx < len(s) and "0" <= s[idx] <= "9":
            res = 10 * res + (ord(s[idx]) - ord("0"))
            
            if res > (2**31 - 1):
                return sign * (2**31 - 1) if sign == 1 else -2**31
                
            idx += 1
            
        return res * sign
s = Solution()
print(s.myAtoi("42")) # 42