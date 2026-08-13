class Solution:

    def encode(self, strs: List[str]) -> str:
        result = ""
        for word in strs:
            result += str(len(word)) + "#" + word
        return result

    def decode(self, s: str) -> List[str]:
        print(s)
        results = []
        i,j = 0,0
        while j < len(s):
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            print(int(length))
            results.append(s[j+1:j+1+length])
            i = j + length + 1
            j = i
        return results