import heapq
from collections import deque

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        # create frequency map
        freq_map = {}

        for t in tasks:
            if t not in freq_map:
                freq_map[t] = 1
            else:
                freq_map[t] += 1

        # put everything on heap -> available
        # (left_tasks, task_type)
        heap = [(freq, key) for key, freq in freq_map.items()]
        heapq.heapify_max(heap)

        # create queue for cooldown
        # (left_tasks, task_type, time2move)
        queue = deque()

        time = 0

        while len(heap) > 0 or len(queue) > 0:
            if len(heap) > 0:
                left_tasks, task_type = heapq.heappop_max(heap)
                if left_tasks > 1:
                    queue.appendleft((left_tasks-1, task_type, time+n))

            while len(queue) > 0 and queue[-1][2] <= time:
                left_tasks, task_type, time2move = queue.pop()
                heapq.heappush_max(heap, (left_tasks, task_type))

            time += 1

        return time
        