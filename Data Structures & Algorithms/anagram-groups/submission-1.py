class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}

        for w in strs:
            ordMap = [0] * 26
            for l in w:
                ordMap[ord(l)-ord('a')] += 1
            ordMap = tuple(ordMap)
            if ordMap in res:
                res[ordMap].append(w)
            else:
                res[ordMap] = [w]
        

        return(list(res.values()))