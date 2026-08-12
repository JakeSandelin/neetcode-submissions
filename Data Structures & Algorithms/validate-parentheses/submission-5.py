class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        closeMap = {"}":"{",")":"(","]":"["}
        
        for l in s:
            if l in closeMap:
                if seen and seen[-1] == closeMap[l]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(l)
        
        return seen == []


            