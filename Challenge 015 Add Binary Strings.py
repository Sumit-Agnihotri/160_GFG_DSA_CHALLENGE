def trimLeadingZeros(s):
    firstOne = s.find("1")
    return s[firstOne:] if firstOne != -1 else "0"
    
class Solution:
	def addBinary(self, s1, s2):
		s1 = trimLeadingZeros(s1)
		s2 = trimLeadingZeros(s2)
		n = len(s1)
		m = len(s2)
		
		if n < m:
			s1, s2 = s2, s1
			n, m = m, n
		j = m - 1
		carry = 0
		result = []
		
		for i in range(n - 1, -1, -1):
			bit1 = int(s1[i])
			bitSum = bit1 + carry
			
			if j >= 0:
				bit2 = int(s2[j])
				bitSum += bit2
				j -= 1
			
			bit = bitSum % 2
			carry = bitSum // 2
			
			result.append(str(bit))
			
		if carry > 0:
			result.append("1")
			
		return "".join(result[::-1])
 
s = Solution()
print(s.addBinary("1101", "111"))  # Output: "10100"