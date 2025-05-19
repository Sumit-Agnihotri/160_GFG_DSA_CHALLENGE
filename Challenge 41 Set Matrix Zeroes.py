mat = [[1, -1, 1],[-1, 0, 1],[1, -1, 1]]

class Solution:
    def setMatrixZeroes(self, mat):
        n,m=len(mat),len(mat[0])
        fz=any(mat[0][j]==0 for j in range(m))
        fc=any(mat[i][0]==0 for i in range(n))
        for i in range(1,n):
            for j in range(1,m):
                if mat[i][j]==0:
                    mat[i][0]=0
                    mat[0][j]=0
        for i in range(1,n):
            for j in range(1,m):
                if mat[i][0]==0 or mat[0][j]==0:
                    mat[i][j]=0
        if fz:
            for j in range(m):
                mat[0][j]=0
        if fc:
            for i in range(n):
                mat[i][0]=0
        return mat
    
s = Solution()
print(s.setMatrixZeroes(mat))
# [[1, 0, 1], [0, 0, 0], [1, 0, 1]]