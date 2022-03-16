from ast import List
import bisect

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res, prefix, idx = [], '', 0
        for ch in searchWord:
            prefix += ch
            idx = bisect.bisect_left(products, prefix, idx)
            res.append([w for w in products[idx: idx + 3] if w.startswith(prefix)])
        return res