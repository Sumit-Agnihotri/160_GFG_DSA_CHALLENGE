start = [1, 3, 0, 5, 8, 5]
finish = [2, 4, 6, 7, 9, 9]

class Solution:
    def activity_selection(self, start, finish):
        acts = sorted(zip(finish, start))
        if not acts:
            return 0
        cnt, last = 1, acts[0][0]
        for f, s in acts[1:]:
            if s > last:
                cnt += 1
                last = f
        return cnt

s = Solution()
print(s.activity_selection(start, finish)) # Output: 4