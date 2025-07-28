arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]

class Solution:
	def minJumps(self, arr):
		n = len(arr)
		if n <= 1: return 0
		if arr[0] == 0: return -1
		jumps, currEnd, farthest = 0, 0, 0
		for i in range(n - 1):
			farthest = max(farthest, i + arr[i])
			if i == currEnd:
				jumps += 1
				currEnd = farthest
				if currEnd >= n - 1:
					break
		return jumps if currEnd >= n - 1 else -1

s = Solution()
print(s.minJumps(arr))  # Output: 3