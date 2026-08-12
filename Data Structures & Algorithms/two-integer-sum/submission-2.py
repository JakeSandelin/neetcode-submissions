class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numMap = {}

        for i,num in enumerate(nums):
            goal = target - num
            if goal in numMap:
                return [numMap[goal],i]
            numMap[num] = i