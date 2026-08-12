class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s2, t2 = [0]* 32, [0] * 32

        for i in range(len(s)):
            s2[ord(s[i])-ord('a')] += 1
            t2[ord(t[i])-ord('a')] += 1


        return s2 == t2