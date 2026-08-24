class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            res,dig = "",""
            if char == "]":
                while stack[-1] != "[":
                    res = stack.pop() + res
                stack.pop()
                while stack and stack[-1].isdigit():
                    dig = stack.pop() + dig
                dig = int(dig)
                stack.append(res * dig)
                continue
            stack.append(char)
        return "".join(stack)
        
