class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = [0] *len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and stack[-1][1] < t:
                i2, t2 = stack.pop()
                temp[i2] = i -i2
            stack.append([i,t])
        
        return temp
