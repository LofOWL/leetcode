from ast import List
import collections
import itertools

class Solution:
    def mostVisitedPattern(self, username: List[str], timestamp: List[int], website: List[str]) -> List[str]:
        pattern = list(zip(username, timestamp, website))
        pattern.sort()
        dic1 = collections.defaultdict(list)
        for i, j, k in pattern:
            dic1[i].append(k)
        dic2 = collections.defaultdict(set)
        for i, j in dic1.items():
            for c in itertools.combinations(j,3):
                dic2[c].add(i)
        return sorted(dic2.items(), key = lambda x: (-len(x[1]), x[0]))[0][0]
