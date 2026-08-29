class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] *len(temperatures)
        pending = [] #temp, ind

        for i, t in enumerate(temperatures):
            while pending and t > pending[-1][1]:
                i2, t2 = pending.pop()
                res[i2] = (i-i2)
            pending.append([i,t])
        return res
