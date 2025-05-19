arr1 = [2, 3, 6, 7, 9]
arr2 = [1, 4, 8, 10]
k = 5

class Solution:
    def kthElement(self,arr1,arr2,k):
        i=j=0
        while True:
            if i==len(arr1):
                return arr2[j+k-1]
            if j==len(arr2):
                return arr1[i+k-1]
            if k==1:
                return min(arr1[i], arr2[j])
            
            idx=k//2-1
            new_i=min(i+idx,len(arr1)-1)
            new_j=min(j+idx,len(arr2)-1)
            if arr1[new_i]<=arr2[new_j]:
                k-=new_i-i+1
                i=new_i+1
            else:
                k-=new_j-j+1
                j=new_j+1
            
s = Solution()
print(s.kthElement(arr1, arr2, k)) # Output: 6