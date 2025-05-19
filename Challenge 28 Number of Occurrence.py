arr = [1, 1, 2, 2, 2, 2, 3]
target = 2

def first_occurrence(arr, x):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            result = mid
            high = mid - 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return result

def last_occurrence(arr, x):
    low, high = 0, len(arr) - 1
    result = -1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == x:
            result = mid
            low = mid + 1
        elif arr[mid] < x:
            low = mid + 1
        else:
            high = mid - 1
    return result
    
class Solution:
    def countFreq(self, arr, x):
        first = first_occurrence(arr, x)
        if first == -1:
            return 0
        last = last_occurrence(arr, x)
        return last - first + 1
    
s = Solution()
result = s.countFreq(arr, target)
print("Number of occurrences of", target, "is:", result) # Output: 4