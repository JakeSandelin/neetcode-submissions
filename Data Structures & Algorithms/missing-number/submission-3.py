class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()

        for i in range(len(nums)):
            if i == 0:
                if nums[0] != 0: return 0
            else:
                if nums[i-1]+1 != nums[i]:
                    return nums[i]-1
        
        return len(nums)