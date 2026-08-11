class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        result = ""
        for i in range(len(word)):
            for str in strs:
                if i >= len(str) or str[i] != word[i]:
                    return result
            result += word[i]
        return result