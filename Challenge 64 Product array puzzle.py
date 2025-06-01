arr = [10, 3, 5, 6, 2]

class Solution:
    def productExceptSelf(self, arr):
        zeros = 0
        idx = -1
        prod = 1
        for i in range(len(arr)):
            if arr[i] == 0:
                zeros += 1
                idx = i
            else:
                prod *= arr[i]
        res = [0] * len(arr)
        
        for i in range(len(arr)):    
            if zeros == 0:
                 res[i] = prod // arr[i]
            elif zeros == 1:
                res[idx] = prod
        return res

s = Solution()
print(s.productExceptSelf(arr)) # Output : [180, 600, 360, 300, 900]