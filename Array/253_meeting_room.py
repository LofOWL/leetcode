from ast import List
from heapq import heappop, heappush
class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x:x[0])
        q=[]
        for x in intervals:
            if q and q[0]<=x[0]: heappop(q)
            heappush(q,x[1])
        return len(q)