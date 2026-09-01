class Solution:
    def isPalindrome(self, s: str) -> bool:
        s2 = ""
        s3 = ""

        for l in s:
            if l.isalnum():
                s2 += l.lower()
                s3 = l.lower() + s3

        
        return s2 == s3