class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        for num in nums:
            numMap[num] = numMap.get(num, 0) + 1
        
        res = sorted(numMap.items(),key=lambda item: item[1], reverse=True)

        return  [num[0] for num in res][:k]