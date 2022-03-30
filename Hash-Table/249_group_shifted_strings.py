from ast import List
from collections import defaultdict

class Solution:
    def calcHash(self, string: str) -> str:
        res = []
        for i in range(len(string) - 1):
            diff = (ord(string[i+1]) - ord(string[i])+26) % 26
            res.append(chr(diff+97))
        return ''.join(res)

    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        dd = defaultdict(list)
        for s in strings:
            h = self.calcHash(s)
            dd[h].append(s)
        res = []
        for v in dd.values():
            res.append(v)
        return res