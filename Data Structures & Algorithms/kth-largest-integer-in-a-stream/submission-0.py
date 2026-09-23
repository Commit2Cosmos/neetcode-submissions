import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k, self.heap = k, nums
        heapq.heapify(self.heap)
        # remove elements below k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        while len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]