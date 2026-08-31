class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        res = defaultdict(int)

        for l in s:
            res[l] += 1

        for l in t:
            res[l] -= 1


        values = list(res.values())

        for value in values:
            if value != 0:
                return False
        
        return True
