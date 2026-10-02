import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        min_heap = []

        for i in range(len(nums)):
            if len(min_heap) == k:
                if nums[i] > min_heap[0]:
                    heapq.heappushpop(min_heap, nums[i])
            else:
                heapq.heappush(min_heap, nums[i])

        return min_heap[0]