class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cMap = defaultdict(int)
        res = 0

        l = 0
        maxC = 0

        for r in range(len(s)):
            cMap[s[r]] += 1

            maxC = max(maxC, cMap[s[r]])

            while ((r-l)+1) > maxC +k:
                cMap[s[l]] -= 1
                l += 1
            
            res = max(res, (r-l)+1)


        return res

            
