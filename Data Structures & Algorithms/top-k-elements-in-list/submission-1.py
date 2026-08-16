class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kMap = defaultdict(int)
        res = []

        for num in nums:
            kMap[num] += 1

        
        items = list(kMap.items())

        items.sort(key = lambda x: x[1],reverse = True)

        for x in range(k):
            res.append(items[x][0])

        return res