class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for word in arr:
            if word == "..":
                if stack:
                    stack.pop()
            elif word != "" and word != ".":
                stack.append(word)
        return ("/" + "/".join(stack)) if len(stack) else "/"
            
