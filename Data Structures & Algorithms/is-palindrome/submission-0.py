class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean_sentence = re.sub(r'[^A-Za-z0-9]',"",s).lower()
        i,j = 0,len(clean_sentence)-1
        while i<j:
            if clean_sentence[i] != clean_sentence[j]:
                return False
            i+=1
            j-=1
        return True