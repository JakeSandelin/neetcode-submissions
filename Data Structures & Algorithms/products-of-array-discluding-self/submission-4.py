class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        total = 1
        for num in nums:
            res.append(total)
            total *= num
            # print(total)

    #    print(res)

        total = 1
        i = len(nums)-1
        for num in reversed(nums):
            res[i] *= total
            total *= num
            i -= 1
            # print(total)

        return res
            
