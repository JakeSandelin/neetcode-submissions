class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sH, tH = {}, {}

        for i in range(len(s)):
           sH[s[i]] = sH.get(s[i],0) + 1
           tH[t[i]] = tH.get(t[i],0) + 1

        return sH == tH