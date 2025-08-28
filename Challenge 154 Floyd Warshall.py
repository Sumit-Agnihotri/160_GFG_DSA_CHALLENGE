dist = [[0, 4, 10 ** 8, 5, 10 ** 8], [10 ** 8, 0, 1, 10 ** 8, 6], [2, 10 ** 8, 0, 3, 10 ** 8], [10 ** 8, 10 ** 8, 1, 0, 2], [1, 10 ** 8, 10 ** 8, 4, 0]]

class Solution:
	def floydWarshall(self, dist):
		n = len(dist)
		INF = 10 ** 8
		for k in range(n):
			for i in range(n):
				for j in range(n):
					if dist[i][k] < INF and dist[k][j] < INF:
						dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
		return dist

s = Solution()
print(s.floydWarshall(dist)) # Output: [[0, 4, 5, 5, 7], [3, 0, 1, 4, 6], [2, 6, 0, 3, 5], [3, 7, 1, 0, 2], [1, 5, 5, 4, 0]]