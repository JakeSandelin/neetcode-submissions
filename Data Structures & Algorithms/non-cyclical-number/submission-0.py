class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        nStr = str(n)
        while nStr != '1':
            num = 0
            for digit in nStr:
                print(digit, num)
                num += int(digit) ** 2
            if num in seen:
                return False
            else:
                seen.add(num)
            nStr = str(num)
        return True