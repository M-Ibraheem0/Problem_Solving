from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        results = []
        counted_arr = Counter(nums).most_common()
        for i in range(k):
            results.append(counted_arr[i][0])
        return results