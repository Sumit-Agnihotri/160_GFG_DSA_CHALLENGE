arr = [12, 34, 67, 90]
k = 2

def check(arr,k,pageLimit):
    count=1
    pageSum=0
    for pages in arr:
        if pageSum+pages>pageLimit:
            count+=1
            pageSum=pages
        else:
            pageSum+=pages
    return count<=k
    
class Solution:
    def findPages(self, arr, k):
        if k>len(arr):
            return -1
        low=max(arr)
        high=sum(arr)
        res=-1
        while low<=high:
            mid=low+(high-low)//2
            if check(arr,k,mid):
                res=mid
                high=mid-1
            else:
                low=mid+1
        return res
    
sol=Solution()
print(sol.findPages(arr,k)) # Output: 113