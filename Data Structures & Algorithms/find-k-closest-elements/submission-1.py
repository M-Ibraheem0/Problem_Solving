class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        currSum,bestSum,l,best_l = 0,float('inf'),0,0
        for r in range(len(arr)):
            currSum += abs(x - arr[r])
            if r - l + 1 > k:
                currSum -= abs(x - arr[l])
                l += 1
            if r - l + 1 == k and currSum < bestSum:
                best_l = l
                bestSum = currSum
        return arr[best_l:best_l + k]
