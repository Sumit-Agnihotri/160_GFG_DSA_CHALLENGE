intervals = [[1, 2], [2, 3], [3, 4], [1, 3]]

class Solution:
    def minRemoval(self, intervals):
        count = 0
        intervals.sort(key=lambda x: x[1])
        end  = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                count += 1
            else:
                end = intervals[i][1]
        
        return count
    
s = Solution()
print(s.minRemoval(intervals)) # Output: 1