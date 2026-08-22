class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closed_brackets = {"]":"[",")":"(","}":"{"}
        for char in s:
            if char not in closed_brackets:
                stack.append(char)
            else:
                if len(stack) > 0 and closed_brackets[char] == stack[-1]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0