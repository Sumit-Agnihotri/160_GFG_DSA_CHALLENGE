arr = [1, 2, 3, 2, 1, 4]

class Solution:
	def singleNum(self, arr):
		x = 0
		for n in arr: x ^= n
		rs = x&-x
		a = b = 0
		for n in arr:
			if n&rs: a ^= n
			else: b ^= n
		return sorted([a, b])

s = Solution()
print(s.singleNum(arr)) # [3, 4]