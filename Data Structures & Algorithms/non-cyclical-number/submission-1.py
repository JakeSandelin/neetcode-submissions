class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        def sumSquares(n):
            s = str(n)
            tot = 0
            for l in s:
                tot += int(l)*int(l)
            
            return tot
        
        while n != 1:
            if n in seen:
                return False
            seen.add(n)
            
            n = sumSquares(n)
        
        return True

        