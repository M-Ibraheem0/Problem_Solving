class Solution:
    def validPalindrome(self, s: str) -> bool:
        clean_string = re.sub('r[^a-zA-Z0-9]','',s)
        i,j = 0,len(s) - 1
        while i<j:
            if s[i] != s[j]:
                return (self.chance(s,i+1,j) | self.chance(s,i,j-1))
            i += 1
            j -= 1
        return True
    def chance(self,s,left,right):
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
        return True