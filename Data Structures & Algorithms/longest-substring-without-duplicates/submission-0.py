from collections import defaultdict
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen,i,j,longest = defaultdict(int),0,0,0
        while j < len(s):
            seen[s[j]] += 1
            while seen[s[j]] > 1:
                seen[s[i]] -= 1
                i += 1
            longest = max(j - i + 1,longest)
            j += 1
        return longest