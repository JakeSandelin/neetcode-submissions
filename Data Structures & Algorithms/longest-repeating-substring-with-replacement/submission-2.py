class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        l = 0
        seen = defaultdict(int)
        maxC = 0
        for r in range(len(s)):
            seen[s[r]] += 1
            
            while r-l-k > maxC:
                seen[s[l]] -= 1
                l+= 1
            maxC = max(seen[s[r]],maxC)
            # longest = max()

        return min(len(s),maxC+k)
