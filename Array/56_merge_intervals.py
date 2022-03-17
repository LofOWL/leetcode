
from ast import List


class Solution:

    def merge(self, intervals:List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x:x[0])
        res = []
        left = intervals[0][0]
        right = intervals[0][1]
        for i in intervals[1:]:
            if i[0] <= right:
                if i[1] > right:
                    right = i[1]
            else:
                res.append([left,right])
                left = i[0]
                right = i[1]
        res.append([left,right])