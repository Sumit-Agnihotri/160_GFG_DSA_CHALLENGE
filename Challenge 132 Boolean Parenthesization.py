s = "T|T&F^T"

class Solution:
    def countWays(self, s):
        memo = {}
        
        def dp(i, j, isTrue):
            if i == j:
                if isTrue:
                    return 1 if s[i] == "T" else 0
                else:
                    return 1 if s[i] == "F" else 0
                
            if (i, j, isTrue) in memo:
                return memo[(i, j, isTrue)]
                
            ways = 0
            for k in range(i+1, j, 2):
                op = s[k]
                lt = dp(i, k-1, True)
                lf = dp(i, k-1, False)
                rt = dp(k+1, j, True)
                rf = dp(k+1, j, False)
                
                if op == "&":
                    ways += lt*rt if isTrue else (lt*rf + lf*rt + lf*rf)
                elif op == "|":
                    ways += (lt*rt + lt*rf + lf*rt) if isTrue else lf*rf
                elif op == "^":
                    ways += (lt*rf + lf*rt) if isTrue else (lt*rt + lf*rf)
                    
            memo[(i, j, isTrue)] = ways
            return memo[(i, j, isTrue)]
            
        return dp(0, len(s) - 1, True)

sol = Solution()
print(sol.countWays(s))  # Output: 4