class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        deque_arr = collections.deque()
        l = 0
        result = []
        for r in range(len(nums)):
            while deque_arr and nums[r] >= nums[deque_arr[-1]]:
                deque_arr.pop()
            deque_arr.append(r)  # store index only, not value
            if deque_arr[0] < l:
                deque_arr.popleft()
            if r - l + 1 == k:
                result.append(nums[deque_arr[0]])
                l += 1
        return result