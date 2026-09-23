"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        count = 0
        res = 0

        start = [t.start for t in intervals]
        end = [t.end for t in intervals]

        start.sort()
        end.sort()

        s_point = 0
        e_point = 0

        while s_point < len(intervals):
            if start[s_point] < end[e_point]:
                count += 1
                s_point += 1
                res = max(res, count)

            else:
                count -= 1
                e_point += 1
            

        return res