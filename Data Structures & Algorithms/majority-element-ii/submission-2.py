from collections import defaultdict
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        results = []
        count = defaultdict(int)
        for num in nums:
            count[num] += 1
            if len(count) <= 2:
                continue
            new_count = defaultdict(int)
            for k,v in count.items():
                if v > 1:
                    new_count[k] = v - 1
            count = new_count
        for num in count:
            if nums.count(num) > len(nums)//3:
                results.append(num)
        return results 
                