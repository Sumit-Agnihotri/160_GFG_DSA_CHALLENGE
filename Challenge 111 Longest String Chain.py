words = ["ba", "b", "a", "bca", "bda", "bdca"]

class Solution:
    def longest_string_chain(self, words):
        words.sort(key = len)
        dp = {}
        res = 1
        for w in words:
            dp[w] = 1
            for i in range(len(w)):
                pre = w[:i] + w[i + 1:]
                if pre in dp:
                    dp[w] = max(dp[w], dp[pre] + 1)
            res = max(res, dp[w])
        return res

s = Solution()
print(s.longest_string_chain(words))  # Output: 4