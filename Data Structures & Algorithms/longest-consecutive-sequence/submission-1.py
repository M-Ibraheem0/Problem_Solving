class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elements = set(nums)
        longest_seq = 1
        for num in nums:
            if (num - 1) in elements:
                continue
            values = 1
            while(num + 1) in elements:
                values += 1
                num += 1
            longest_seq = max(longest_seq,values)
        return longest_seq
