class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix,suffix,products = [1] * len(nums),[1] * len(nums),[1] * len(nums)
        n = len(nums) - 1
        for i in range(1,len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
            suffix[-i-1] = suffix[n] * nums[n]
            n -= 1
        for i in range(len(prefix)):
            products[i] = prefix[i] * suffix[i]
        return products
