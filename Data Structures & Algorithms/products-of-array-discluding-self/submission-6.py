class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = nums.copy()

        total = 1
        for i, num in enumerate(nums):
            res[i] = total
            total = num *total

        #res = res[::-1]
        total = 1
        for i in reversed(range(len(nums))):
            res[i] *= total
            total = nums[i] *total
        return res