from typing import (
    List,
)
from lintcode import (
    Interval,
)

"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: if a person could attend all meetings
    """
    def can_attend_meetings(self, intervals: List[Interval]) -> bool:
        # Write your code here
        intervals.sort(key=lambda x: x.start)
        for i in range(len(intervals) - 1):
            current_meeting = intervals[i]
            next_meeting = intervals[i + 1]
            if next_meeting.start < current_meeting.end:
                return False
        
        return True