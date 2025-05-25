from collections import defaultdict

arr = [1, 2, 1, 3, 4, 2, 3]
k = 4

class Solution:
    def countDistinct(self, arr, k):
        n = len(arr)
        res = []
        freq = defaultdict(int)
        
        for i in range(k):
            freq[arr[i]] += 1
            
        res.append(len(freq))
            
        for i in range(k, n):
            freq[arr[i]] += 1
            freq[arr[i - k]] -= 1
                
            if freq[arr[i - k]] == 0:
                del freq[arr[i - k]]
                    
            res.append(len(freq))
        return res

s = Solution()
print(s.countDistinct(arr, k))  # Output: [3, 4, 4, 3]