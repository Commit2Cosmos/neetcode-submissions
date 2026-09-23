import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = stones
        heapq.heapify_max(stones)
        while len(stones) > 1:
            first_largest = heapq.heappop_max(heap)
            second_largest = heapq.heappop_max(heap)

            diff = abs(first_largest - second_largest)

            if diff == 0:
                continue
            
            heapq.heappush_max(heap, diff)

        if len(heap) == 0:
            return 0

        return heap[0]
            