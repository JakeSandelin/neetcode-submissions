class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones2 = []
        for stone in stones:
            stones2.append(stone*-1)

        heapq.heapify(stones2)


        while len(stones2) > 1:
            s1 = heapq.heappop(stones2) *-1
            s2 = heapq.heappop(stones2) *-1
            r = (s1-s2) * -1
            heapq.heappush(stones2, r)


        return heapq.heappop(stones2) * -1 if stones2 else 0



