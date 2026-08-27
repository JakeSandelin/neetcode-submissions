class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_o = [0] *32
        s2_o = [0] *32
        for l in s1:
            s1_o[ord(l)-ord('a')]+=1

        l=0
        for r in range(len(s2)):
            s2_o[ord(s2[r])-ord('a')]+=1
            if (r-l)+1 >len(s1):
                s2_o[ord(s2[l])-ord('a')]-=1
                l+=1
            if s1_o == s2_o:
                return True
        
        return False
