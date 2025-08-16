g = [[0, 1, 2], [0, 1, 2], [2, 1, 1]]

from collections import deque

class Solution:
	def orangesRotting(self, g):
		n, m, lenf = len(g), len(g[0]), 0
		q = deque()
		for i in range(n):
			for j in range(m):
				if g[i][j] == 2:
					q.append((i, j, 0))
				if g[i][j] == 1:
					lenf += 1
		t = 0
		while q:
			i, j, t = q.popleft()
			for x, y in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
				if 0 <= i + x < n and 0 <= j + y < m and g[i + x][j + y] == 1:
					g[i + x][j + y] = 2
					lenf -= 1
					q.append((i + x, j + y, t + 1))
		return -1 if lenf else t

s = Solution()
print(s.orangesRotting(g))  # Output: 1