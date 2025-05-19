mat = [[1, 5, 9], [14, 20, 21], [30, 34, 43]]
x = 14

class Solution:
    def searchMatrix(self, mat, x):
        n = len(mat)
        m = len(mat[0])
        
        low, high = 0, n * m - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // m
            col = mid % m
            if mat[row][col] == x:
                return True
            elif mat[row][col] < x:
                low = mid + 1
            else:
                high = mid - 1
        
        return False
    
s = Solution()
result = s.searchMatrix(mat, x)
print(result)  # Output: True