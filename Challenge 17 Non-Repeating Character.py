input_string = "geeksforgeeks"

max_char = 26

class Solution:
    def nonRepeatingChar(self, s):
        vis = [-1] * max_char
        for i in range(len(s)):
            if vis[ord(s[i]) - ord("a")] == -1:
               vis[ord(s[i]) - ord("a")] = i
            else:
                vis[ord(s[i]) - ord("a")] = -2
        idx = float("inf")
        for i in range(max_char):
            if vis[i] >= 0:
                idx = min(idx, vis[i])
            
        return "$" if idx == float("inf") else s[idx]
    
solution = Solution()
print(solution.nonRepeatingChar(input_string)) # Output: "f"