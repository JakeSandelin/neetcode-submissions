class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen, res = set(), set(nums)

        for num in nums:
            if num in seen and num in res:
                res.remove(num)
                continue
            else:
                seen.add(num)
        

        return res.pop()
            