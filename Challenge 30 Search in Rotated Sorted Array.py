arr = [5, 6, 7, 8, 9, 10, 1, 2, 3]
key = 3

class Solution:
    def search(self,arr,key):
        low = 0
        high = len(arr) - 1
        
        while low <= high:
            mid = low + (high - low) // 2
            if arr[mid] == key:
                return mid
            if arr[mid] >= arr[low]:
                if key >= arr[low] and key < arr[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if key > arr[mid] and key <= arr[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
    
s = Solution()
result = s.search(arr, key)
print(f"Element {key} is found at index: {result}") if result != -1 else print(f"Element {key} is not found in the array.") # Output: Element 3 is found at index: 8