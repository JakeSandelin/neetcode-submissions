class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        bInd = True
        marker = len(digits)-1

        while bInd:
            if digits[marker] == 9:
                if marker == 0:
                    digits[marker] = 0
                    digits.insert(0,1)
                    bInd = False
                else:
                    digits[marker] = 0
                    marker -= 1
            else:
                digits[marker] += 1
                bInd = False

        return digits



