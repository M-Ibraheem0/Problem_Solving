class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {}
        for i,num in enumerate(nums):
            if num in num_map and abs(num_map[num] - i) <= k:
                return True
            num_map[num] = i
        return False
            
