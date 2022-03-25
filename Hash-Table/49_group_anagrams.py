from ast import List
import collections


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if not strs:
            return []
        result = collections.defaultdict(list)
        for str in strs:
            key = ''.join(sorted(str))
            result[key].append(str)
        return list(result.values())