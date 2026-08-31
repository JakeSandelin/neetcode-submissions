class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = defaultdict(int)

        for l in s:
            seen[l] += 1

        for l in t:
            seen[l] -= 1


        values = list(seen.values())


        for val in values:
            if val != 0:
                return False
        return True