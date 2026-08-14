class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sNum = ""
        number = 0
        for num in digits:
            sNum += str(num)
        
        number = int(sNum) +1
        sNum = str(number)

        res = []

        for num in sNum:
            res.append(num)

        return res
         
