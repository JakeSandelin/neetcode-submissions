class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        cMap = defaultdict(int)

        l, cMax = 0, 0
        res = 0

        for r in range(len(s)):
            cMap[s[r]] += 1

            cMax = max(cMax, cMap[s[r]])
            while  ((r-l)+1) > cMax +k:
                cMap[s[l]] -= 1
                l +=1
            
            res = max(res,((r-l)+1))
        return res
