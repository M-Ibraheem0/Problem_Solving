from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        n = len(nums)
        counts = Counter(nums).most_common()
        results = []
        for count in counts:
            if len(results) >= 2:
                return results
            if count[1] > n / 3:
                results.append(count[0])
        return results