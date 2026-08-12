class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for j, num in enumerate(nums):
            goal = target - num
            if goal in seen:
                return([seen[goal],j])
            else:
                seen[num] = j