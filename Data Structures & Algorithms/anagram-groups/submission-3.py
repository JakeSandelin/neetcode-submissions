class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for word in strs:
            key = [0] *28
            for l in word:
                key[ord(l)-ord('a')] += 1

            if tuple(key) in groups:
                groups[tuple(key)].append(word)
            else:
                groups[tuple(key)] = [word]

        return list(groups.values())
            
