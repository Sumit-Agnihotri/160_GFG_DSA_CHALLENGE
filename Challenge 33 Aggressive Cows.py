stalls = [1, 2, 4, 8, 9]
k = 3

def canPlaceCows(stalls, k, dist):
        count=1
        previous=stalls[0]
        for i in range(1, len(stalls)):
            if stalls[i]-previous>=dist:
                previous=stalls[i]
                count+=1
        
        return count>=k
            
class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        res=0
        low=1
        high=stalls[-1]-stalls[0]
        while low<=high:
            mid=low+(high-low)//2
            if canPlaceCows(stalls, k, mid):
                res=mid
                low=mid+1
            else:
                high=mid-1
        return res
    
s =Solution()
print(s.aggressiveCows(stalls, k)) # Output: 3