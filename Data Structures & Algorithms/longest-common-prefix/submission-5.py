class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        first_word = strs[0]
        result = ""
        for i in range(len(first_word)):
            for word in strs:
                if i >= len(word) or word[i] != first_word[i]:
                    return result
            result += first_word[i]
        return result