mat = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

class Solution:
    def rotateby90(self, mat):
        n = len(mat)
        for row in mat:
            row.reverse()
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]

s = Solution()
s.rotateby90(mat)
for row in mat:
    print(row)