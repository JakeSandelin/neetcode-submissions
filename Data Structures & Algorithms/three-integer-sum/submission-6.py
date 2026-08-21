class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        print(nums)
        for i, a in enumerate(nums):
            l,r = i+1,len(nums)-1

            if i != 0 and a == nums[i-1]:
                continue
        
            while l<r:
                if a + nums[l] + nums[r] > 0:
                    r -=1
                    while nums[r] == nums[r+1] and l<r:
                        # print("Wow")
                        r -= 1
                elif a + nums[l] + nums[r] < 0:                
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        # print("here")
                        l += 1
                else:
                    # print(i,l,r)
                    res.append([a,nums[l],nums[r]])
                    l += 1
                    while nums[l] == nums[l-1] and l<r:
                        #print("there")
                        l += 1

        return list(res)

            