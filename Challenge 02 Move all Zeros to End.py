arr = [3,5,0,0,4]

class Solution:
	def pushZerosToEnd(self, arr):
		count = 0
		for i, value in enumerate(arr):
			if value != 0:
				arr[i], arr[count] = arr[count], arr[i]
				count += 1

sol = Solution()
sol.pushZerosToEnd(arr)
print("After: ", arr)