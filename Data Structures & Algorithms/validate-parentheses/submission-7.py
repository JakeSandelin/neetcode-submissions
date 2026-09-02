class Solution:
    def isValid(self, s: str) -> bool:
        pair = {"}":"{","]":"[",")":"("}
        stack = []

        for i in s:
            if i in pair:
                if stack and pair[i] == stack[-1]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)

        return True if stack == [] else False