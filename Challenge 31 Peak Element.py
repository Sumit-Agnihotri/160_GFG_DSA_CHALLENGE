arr = [1, 2, 4, 5, 7, 8, 3]

class Solution:   
    def peakElement(self,arr):
        n=len(arr)
        if n==1:
            return 0
        
        if arr[0]>=arr[1]:
            return 0
        
        if arr[n-1]>=arr[n-2]:
            return n-1
        
        low, high=1, n-2
        while low<=high:
            mid=low+(high-low)//2
            if arr[mid]>arr[mid-1] and arr[mid]>arr[mid+1]:
                return mid
            if arr[mid]<arr[mid+1]:
                low=mid+1
            else:
                high=mid-1
                
s = Solution()
result = s.peakElement(arr)
print(bool(result)) # Output: True if peak element is found, False otherwise
print(result) # Output: Index of the peak element, or -1 if not found