class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for word in strs:
            wLen = len(word)
            encoded += str(wLen) + "%`" + word
        
        return encoded
            

    def decode(self, s: str) -> List[str]:
        strs = []

        cache, p  = "", ""
        l = 0

        while l < len(s): 
            cache += s[l]
            if s[l] == "`" and p == "%":
                length = int(cache[:-2])
                strs.append(s[l+1:l+length+1])
                cache, p = "", ""
                l += length

            p = s[l]
            l += 1

        return strs




