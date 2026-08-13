from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_arr = [[] for _ in range(len(nums) + 1)]
        freq = Counter(nums)
        for g,v in freq.items():
            freq_arr[v].append(g)

        results,i = [],len(freq_arr) - 1
        while len(results) < k :
            if len(freq_arr[i]):
                results += freq_arr[i]
            i -= 1
        return results