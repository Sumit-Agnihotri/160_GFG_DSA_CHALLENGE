s = "((()"

class Solution:
    def max_length(self, s):
        st, res = [-1], 0
        for i, c in enumerate(s):
            if c == "(": st.append(i)
            else:
                st.pop()
                if not st: st.append(i)
                else: res = max(res, i - st[-1])
        return res

sol = Solution()
print(sol.max_length(s)) # Output: 2