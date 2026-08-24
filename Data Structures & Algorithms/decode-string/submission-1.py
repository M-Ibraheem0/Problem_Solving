class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        for char in s:
            if char == "]":
                res,dig = "",""
                while stack[-1] != "[":
                    res = stack.pop() + res
                stack.pop()
                while stack and stack[-1].isdigit():
                    dig = stack.pop() + dig
                stack.append(res * int(dig))
                continue
            stack.append(char)
        return "".join(stack)
        
