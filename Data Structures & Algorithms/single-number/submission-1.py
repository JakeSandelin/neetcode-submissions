class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        candidates = set(nums)

        for num in nums:
            if num in seen:
                candidates.remove(num)
            else:
                seen.add(num)

        return list(candidates)[0]