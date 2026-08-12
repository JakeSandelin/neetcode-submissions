class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        last = None
        
        for num in nums:
            if num == last:
                return True
            last = num
        
        return False