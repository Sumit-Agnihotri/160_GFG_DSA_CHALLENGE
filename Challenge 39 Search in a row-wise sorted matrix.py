mat = [[3, 4, 9],[2, 5, 6],[9, 25, 27]]
x = 9

def search(arr, x):
    low, high = 0, len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if x == arr[mid]:
            return True
        
        if x < arr[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return False

class Solution:
    def searchRowMatrix(self, mat, x):
        n, m = len(mat), len(mat[0])
        for i in range(n):
            if search(mat[i], x):
                return True
        return False

s = Solution()
print(s.searchRowMatrix(mat, x)) # True