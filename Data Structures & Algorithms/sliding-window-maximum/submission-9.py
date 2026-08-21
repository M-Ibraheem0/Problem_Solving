class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        results,deq = [],collections.deque()
        for r in range(len(nums)):
            while len(deq) > 0 and nums[r] >= nums[deq[-1]]:
                deq.pop()
            deq.append(r)
            if r - l + 1 == k:
                results.append(nums[deq[0]])
                if l == deq[0]:
                    deq.popleft()
                l += 1
        return results
                