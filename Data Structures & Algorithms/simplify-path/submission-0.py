class Solution:
    def simplifyPath(self, path: str) -> str:
        arr = path.split("/")
        stack = []
        for word in arr:
            if word == "" or word == ".":
                continue
            elif word == "..":
                if stack:
                    stack.pop()
                else:
                    continue
            else:
                stack.append(word)
        return ("/" + "/".join(stack)) if len(stack) else "/"
            
