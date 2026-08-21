class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""

        for l in s:
            if l.isalnum():
                s2 += l.lower()
        
        return s2 == s2[::-1]