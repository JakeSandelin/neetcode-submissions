class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for word in strs:
            ordMap = [0]*32
            for l in word:
                ordMap[ord(l)-ord('a')] += 1
            
            if tuple(ordMap) in res:
                res[tuple(ordMap)].append(word)
            else:
                res[tuple(ordMap)] = [word]
        
        result = [item for item in res.values()]
        return result