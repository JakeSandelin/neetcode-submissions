class Solution:
    def isValid(self, s: str) -> bool:
        match = {"}":"{","]":"[",")":"("}
        res = []
        for l in s:
            if l in match:
                if res and res[-1] == match[l]:
                    res.pop()
                else:
                    return False
            else:
                res.append(l)
        
        return True if len(res) == 0 else False