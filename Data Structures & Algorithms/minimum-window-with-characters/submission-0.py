from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        needed,l,best_length,best_l = len(t),0,float('inf'),0
        count = Counter(t)
        for r in range(len(s)):
            if s[r] in count:
                count[s[r]] -= 1
                if count[s[r]] >= 0:
                    needed -= 1
            while needed == 0:
                if best_length > r - l + 1:
                    best_length = r - l + 1
                    best_l = l
                if s[l] in count:
                    count[s[l]] += 1
                    if count[s[l]] > 0:
                        needed += 1
                l += 1
        return "" if best_length == float("inf") else s[best_l:best_l + best_length]