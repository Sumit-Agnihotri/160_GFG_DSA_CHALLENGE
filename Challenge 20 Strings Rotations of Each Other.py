def computeLPSArray(pat):
    n = len(pat)
    lps = [0] * n
    patLen = 0
    lps[0] = 0
    i = 1
    while i < n:
        if pat [i] == pat[patLen]:
            patLen += 1
            lps[i] = patLen
            i += 1
        else:
            if patLen != 0:
                patLen = lps[patLen - 1]
            else:
                lps[i] = 0
                i += 1
        return lps
        
class Solution:
    
    #Function to check if two strings are rotations of each other or not.
    def areRotations(self,s1,s2):
        s1 =s1+ s1
        return s2 in s1
    
s = Solution()
s1 = "ABCD"
s2 = "CDAB"
print(s.areRotations(s1, s2))  # Output: True