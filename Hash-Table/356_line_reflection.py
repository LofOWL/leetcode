from ast import List
import collections

class Solution:
    def isReflected(self, points: List[List[int]]) -> bool:
        # 找到每个y对应的x集合，再进行判断
        seen = collections.defaultdict(set)
        line = None
        # 找到每个y下的所有x
        for x, y in points:
            seen[y].add(x)
        for y, x in seen.items():
            cur = sorted(list(x))
            if not line:
                line = (cur[0] + cur[-1]) / 2
            # 双指针判断，是否有当前点的对称点
            l, r = 0, len(cur) - 1
            while l <= r:
                if cur[l] + cur[r] != 2 * line:
                    return False
                l += 1
                r -= 1
        return True
