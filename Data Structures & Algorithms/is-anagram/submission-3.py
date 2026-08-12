class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sList = [0]*26
        tList = [0]*26

        for x in range(len(s)):
            sList[ord(s[x])-ord('a')] += 1
            tList[ord(t[x])-ord('a')] += 1
        
        return sList == tList