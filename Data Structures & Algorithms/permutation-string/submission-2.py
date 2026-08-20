class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        i,j = 0,len(s1)
        s1 = ''.join(sorted(s1))
        while j <= len(s2):
            substr = s2[i:j]
            sorted_substr = ''.join(sorted(substr))
            print(sorted_substr)
            if sorted_substr == s1:
                return True
            i += 1
            j += 1
        return False



