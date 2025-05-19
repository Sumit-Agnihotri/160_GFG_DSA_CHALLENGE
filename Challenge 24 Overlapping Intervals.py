arr = [[1,3],[2,4],[6,8],[9,10]]

class Solution:
	def mergeOverlap(self, arr):
		arr.sort()
		res = []
		res.append(arr[0])
		
		for i in range(1, len(arr)):
			last = res[-1]
			current = arr[i]

			if current[0] <= last[1]:
				last[1] = max(last[1], current[1])
			else:
				res.append(current)
			
		return res

s = Solution()
print(s.mergeOverlap(arr)) # Output: [[1, 4], [6, 8], [9, 10]]C