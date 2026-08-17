class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i = 0
        while i<len(nums):
            if nums[i] <= 0 or nums[i] > len(nums) or nums[nums[i] - 1] == nums[i]:
                print("for",nums[i])
                i += 1
                continue
            correct = nums[i]-1
            nums[i],nums[correct] = nums[correct],nums[i]
            print(nums)
            print("for i",i)
            i-=1


        print(nums)
        val = 1
        for i in range(len(nums)):
            if nums[i] != val:
                return val
            val += 1
        return val         
            

            

