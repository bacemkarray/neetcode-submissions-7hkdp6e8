class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        maxHeap = []
        for stone in stones:
            heapq.heappush(maxHeap, -stone)

        while len(maxHeap) >= 2:
            x = -heapq.heappop(maxHeap)
            y = -heapq.heappop(maxHeap)
            if x > y:
                heapq.heappush(maxHeap, -(x-y))
            elif y < x:
                heapq.heappush(maxHeap, -(y-x))

        return -maxHeap[0] if maxHeap else 0
