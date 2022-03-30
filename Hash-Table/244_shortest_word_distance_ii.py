from ast import List
from collections import defaultdict

class WordDistance:

    def __init__(self, words: List[str]):
        self.dic = defaultdict(list)
        for i,word in enumerate(words):
            self.dic[word].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        res = 0x3f3f3f3f
        pos_1, pos_2 = self.dic[word1], self.dic[word2]
        i, j = 0, 0
        while i < len(pos_1) and j < len(pos_2):        #贪心，两点追追问题
            res = min(res, abs(pos_1[i] - pos_2[j]))
            if pos_1[i] > pos_2[j]:                     #让小的增一增
                j += 1
            else:
                i += 1
        return res
