"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intList = sorted(intervals,key =lambda x: x.start, reverse = False)

        for i in range(len(intervals)-1):
            if intList[i].end >intList[i+1].start:
                return False
        return True
