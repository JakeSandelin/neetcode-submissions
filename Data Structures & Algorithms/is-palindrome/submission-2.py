class Solution:
    def isPalindrome(self, s: str) -> bool:
        new_s = ""

        for l in s:
            if l.isalnum():
                new_s += l.lower()
        

        return new_s == new_s[::-1]