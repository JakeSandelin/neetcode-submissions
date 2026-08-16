class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        kMap = defaultdict(int)

        for num in nums:
            kMap[num] += 1

        res = sorted(list(kMap.items()),key = lambda x: x[1], reverse = True)

        return [val[0] for val in res[:k]]