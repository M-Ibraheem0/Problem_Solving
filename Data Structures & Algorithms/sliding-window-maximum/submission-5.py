class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        l = 0
        max_arr = []
        deque_arr = collections.deque()
        for r in range(len(nums)):
            while len(deque_arr) > 0 and nums[r] >= deque_arr[len(deque_arr) - 1][1]:
                deque_arr.pop()
            deque_arr.append([r,nums[r]])
            if r - l + 1 == k:
                index,max_val = deque_arr[0]
                if l == index and nums[l] == max_val:
                    deque_arr.popleft()
                l += 1
                max_arr.append(max_val)

        return max_arr