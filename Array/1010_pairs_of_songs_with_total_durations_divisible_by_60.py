from ast import List
from collections import Counter

class Solution:
    def numPairsDivisibleBy60(self, t: List[int]) -> int:
        t = [c % 60 for c in t]
        #print(t)
        ct = Counter(t)
        ret = ct[0] * (ct[0]-1) + ct[30] * (ct[30]-1)
        ret //= 2
        ct[0], ct[30] = 0, 0
        #print(ret)
        ret += sum(ct[i]*ct[60-i] for i in ct) //2
        return ret