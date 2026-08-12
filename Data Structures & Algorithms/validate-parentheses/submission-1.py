class Solution:
    def isValid(self, s: str) -> bool:
        valMap = {"}":"{","]":"[",")":"("}
        seen = []
        for l in s:
            if l in valMap and seen:
                if seen[-1] == valMap[l]:
                    seen.pop()
                else:
                    return False
            else:
                seen.append(l)
        
        return seen == []