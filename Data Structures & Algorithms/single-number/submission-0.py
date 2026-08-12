class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = set()
        once = set()

        for num in nums:
            if num in seen and num in once:
                once.remove(num)
            if num not in seen:
                seen.add(num)
                once.add(num)
            
        return list(once)[0]
