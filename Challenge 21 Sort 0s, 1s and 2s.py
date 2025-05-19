arr = [0, 1, 2, 0, 1, 2]

class Solution:
    # Function to sort an array of 0s, 1s, and 2s
    def sort012(self, arr):
        n = len(arr)
        low = 0
        high = n - 1
        mid = 0
        while mid <= high:
            if arr[mid] == 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low = low + 1
                mid = mid + 1
                
            elif arr[mid] == 1:
                mid = mid + 1
                
            else:
                arr[high], arr[mid] = arr[mid], arr[high]
                high = high - 1
            
        return arr

s = Solution()
result = s.sort012(arr)
print(result)  # Output: [0, 0, 1, 1, 2, 2]