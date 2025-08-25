image = [[1, 1, 1, 0], [0, 1, 1, 1], [1, 0, 1, 1]]
sr = 1
sc = 2
newColor = 2

class Solution:
	def floodFill(self, image, sr, sc, newColor):
		old = image[sr][sc]
		if old == newColor:
			return image
		def dfs(r, c):
			if 0 <= r < len(image) and 0 <= c < len(image[0]) and image[r][c] == old:
				image[r][c] = newColor
				dfs(r+1, c)
				dfs(r-1, c)
				dfs(r, c+1)
				dfs(r, c-1)
		dfs(sr, sc)
		return image

s = Solution()
print(s.floodFill(image, sr, sc, newColor)) # Output: [[2,2,2,0],[0,2,2,2],[1,0,2,2]]