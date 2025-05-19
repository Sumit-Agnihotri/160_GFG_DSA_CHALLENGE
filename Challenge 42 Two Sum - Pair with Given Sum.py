arr = [1, 4, 45, 6, 10, 8]
target = 16

class Solution:
	def twoSum(self, arr, target):
	    s = set()
	    for num in arr:
	        complement = target - num
	        if complement in s:
	            return True
	        s.add(num)
	    return False
 
s = Solution()
result = s.twoSum(arr, target)
print(result)  # Output: True