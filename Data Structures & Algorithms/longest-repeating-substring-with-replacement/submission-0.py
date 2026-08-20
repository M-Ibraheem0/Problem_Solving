class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        chars = set(s)
        longest_length = 0
        for char in chars:
            l,replaced = 0,0
            for r in range(len(s)):
                if s[r] != char:
                    replaced += 1
                while replaced > k:
                    if s[l] != char:
                        replaced -= 1
                    l += 1
                longest_length = max(longest_length,r - l + 1)
        return longest_length