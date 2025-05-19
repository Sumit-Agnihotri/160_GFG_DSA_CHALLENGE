arr = [2, 4, 1, 3, 5]

def countAndMerge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]
    res = 0
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            res += (n1 - i)
        k += 1
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1
    return res
def countInv(arr, l, r):
    res = 0
    if l < r:
        m = (r + l) // 2
        res += countInv(arr, l, m)
        res += countInv(arr, m + 1, r)
        res += countAndMerge(arr, l, m, r)
    return res
class Solution:
    def inversionCount(self, arr):
        return countInv(arr, 0, len(arr) - 1)
s = Solution()
print(s.inversionCount(arr)) # Output: 4