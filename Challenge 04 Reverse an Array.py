arr = [1,2,3,4,5]

class Solution:
    #Function to rotate an array by d elements in counter-clockwise direction. 
    def rotateArr(self, arr, d):
        n = len(arr)
        d %= n
        reverse(arr, 0, d - 1)
        reverse(arr, d,n - 1)
        reverse(arr, 0, n - 1)
def reverse(arr,start,end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start+=1
        end-=1
        
s = Solution()
s.rotateArr(arr, 2)
print(arr)