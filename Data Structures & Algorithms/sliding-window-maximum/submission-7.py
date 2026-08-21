class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        max_arr = []
        deque_arr = collections.deque()
        for r in range(len(nums)):
            while len(deque_arr) > 0 and nums[r] >= nums[deque_arr[-1]]:
                deque_arr.pop()
            deque_arr.append(r)
            if r - l + 1 == k:
                max_arr.append(nums[deque_arr[0]])
                if l == deque_arr[0] and nums[l] == nums[deque_arr[0]]:
                    deque_arr.popleft()
                l += 1
        return max_arr