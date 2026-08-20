class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        counting_arr,check_counting = [0] * 26,[0] * 26
        for s in s1:
            counting_arr[ord(s) - ord('a')] += 1
        window,i = len(s1),0
        for r in range(len(s2)):
            if r - i + 1 > window:
                check_counting[ord(s2[i]) - ord('a')] -= 1
                i += 1
            check_counting[ord(s2[r]) - ord('a')] += 1
            if counting_arr == check_counting:
                return True
        return False