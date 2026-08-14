"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals.sort(key = lambda i: i.start)

        for x in range(len(intervals)-1):
            y = x +1
            if intervals[x].end > intervals[y].start:
                return False
        
        return True