arr = [12, 35, 1, 10, 34, 1]

class Solution:
    def second_largest(self,arr):
        n = len(arr)
        if n < 2:
            return -1
    first = second = float("-inf")
    for num in arr:
        if num > first:
            second = first
            first = num
        elif num > second and num != first:
            second = num
    if second == float("-inf"):
        print(-1)
    else:
        print(second)