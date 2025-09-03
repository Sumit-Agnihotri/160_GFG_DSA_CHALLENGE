arr = [8, -8, 9, -9, 10, -11, 12]

def circularSubarraySum(arr):
    Total = 0
    currentMaxSum = 0
    currentMinSum = 0
    minSum = arr[0]
    maxSum = arr[0]
    
    for i in range(len(arr)):
        currentMaxSum = max(currentMaxSum + arr[i], arr[i])
        maxSum = max(maxSum, currentMaxSum)
        
        currentMinSum = min(currentMinSum + arr[i], arr[i])
        minSum = min(minSum, currentMinSum)
        
        Total += arr[i]
        
    normalSum = maxSum
    circularSum = Total - minSum
    
    if minSum == Total:
        return normalSum
        
    return max(normalSum, circularSum)

print(circularSubarraySum(arr)) # Output: 22