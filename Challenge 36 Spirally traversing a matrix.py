mat = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12], [13, 14, 15, 16, 17, 18]]

class Solution:
    def spirallyTraverse(self, mat):
        m, n = len(mat), len(mat[0])
        res = []
        top, bottom, left, right = 0, m - 1, 0, n - 1
        while top <= bottom and left <= right:
            for i in range(left, right + 1):
                res.append(mat[top][i])
            top += 1
            
            for i in range(top, bottom + 1):
                res.append(mat[i][right])
            right -= 1
            
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    res.append(mat[bottom][i])
                bottom -= 1
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    res.append(mat[i][left])
                left += 1
        
        return res

s = Solution()
print(s.spirallyTraverse(mat))  # Output: [1, 2, 3, 4, 5, 6, 12, 18, 17, 16, 15, 14, 13, 7, 8, 9, 10, 11]