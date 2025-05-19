citations = [3, 0, 5, 3, 0]

class Solution:
    # Function to find hIndex
    def hIndex(self, citations):
        n = len(citations)
        freq = [0] * (n + 1)
        for citation in citations:
            if citation >= n:
                freq[n] += 1
            else:
                freq[citation] += 1
                
        idx = n
        
        s = freq[n]
        while s < idx:
            idx -= 1
            s += freq[idx]
            
        return idx
    
s = Solution()
result = s.hIndex(citations)
print(result)  # Output: 3