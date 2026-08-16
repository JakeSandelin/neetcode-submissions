class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if nums[0] != 0:
            return 0
        prev = 0
        for num in nums:
            if num == 0:
                continue
            if num - prev != 1:
                return prev + 1
            prev = num

        return nums[-1] + 1
