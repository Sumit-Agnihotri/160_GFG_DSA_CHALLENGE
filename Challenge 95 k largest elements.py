arr = [12, 5, 787, 1, 23]
k = 2

import heapq

class Solution:
	def k_largest(self, arr, k):
		min_H = arr[:k]
		heapq.heapify(min_H)
		for x in arr[k:]:
			if x > min_H[0]:
				heapq.heapreplace(min_H, x)
		res = []
		while min_H:
			res.append(heapq.heappop(min_H))
		res.reverse()
		return res

s = Solution()
print(s.k_largest(arr, k))  # Output: [787, 23]