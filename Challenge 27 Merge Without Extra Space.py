a = [2, 4, 7, 10]
b = [2, 3]

class Solution:
    # Function to merge the arrays.
    def merge_arrays(self, a, b):
        n, m = len(a), len(b)
        i, j = n - 1, 0
        while i >= 0 and j < m:
            if a[i] <= b[j]:
                break
            # Swap elements between the two arrays
            a[i], b[j] = b[j], a[i]
            i -= 1
            j += 1
        # Sort both arrays
        a.sort()
        b.sort()
        return a, b
    
s = Solution()
result = s.merge_arrays(a, b)
print("Merged arrays:")
print("Array a:", result[0])
print("Array b:", result[1])