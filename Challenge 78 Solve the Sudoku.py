grid = [
    [5, 3, 0, 0, 7, 0, 0, 0, 0],
    [6, 0, 0, 1, 9, 5, 0, 0, 0],
    [0, 9, 8, 0, 0, 0, 0, 6, 0],
    [8, 0, 0, 0, 6, 0, 0, 0, 3],
    [4, 0, 0, 8, 0, 3, 0, 0, 1],
    [7, 0, 0, 0, 2, 0, 0, 0, 6],
    [0, 6, 0, 0, 0, 2, 8, 0, 0],
    [0, 0, 4, 1, 9, 5, 7, 0, 3],
    [1, 2, 0, 0, 0, 0, 0, 0, 0]
]

class Solution:
    def solveSudoku(self, grid):
        def isValid(num, grid, row, col):
            for i in range(9):
                if grid[row][i] == num or grid[i][col] == num:
                    return False
                    
            rr = row - row % 3
            cc = col - col % 3
            
            for i in range(3):
                for j in range(3):
                    if grid[rr + i][cc + j] == num:
                        return False
                        
            return True
            
        def solve():        
            for i in range(9):
                for j in range(9):
                    if grid[i][j] == 0:
                        for num in range(1, 10):
                            if isValid(num, grid, i, j):
                                grid[i][j] = num
                                if solve():
                                    return True
                                grid[i][j] = 0
                        return False
            return True
            
        solve()

s = Solution()
s.solveSudoku(grid)
print("Sudoku solved:")
for row in grid:
    print(row)