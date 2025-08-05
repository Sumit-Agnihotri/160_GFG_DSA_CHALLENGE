digits = "123"

class Solution:
	def countWays(self, digits):
		a = b = 1
		for i in range(1, len(digits)):
			c = (digits[i] != "0") * b + (10 <= int(digits[i-1:i+1]) <= 26) * a
			a, b = b, c
		return b * (digits[0] != "0")

s = Solution()
print(s.countWays("123"))  # Output: 3