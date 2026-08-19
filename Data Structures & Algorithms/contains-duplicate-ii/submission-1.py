class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        num_map = {}
        for i,num in enumerate(nums):
            if num in num_map:
                value = abs(num_map[num] - i)
                if value <= k:
                    return True
                num_map.pop(num)
            num_map[num] = i
        return False
            
