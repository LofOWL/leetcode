from ast import List
from collections import defaultdict

class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        """
        [5,5,9,2,5,5,9,2,2,5,5,6,2,2,5,2,5,4,3], 7, 18
        """
        indexs = defaultdict(list)
        ans = 0
        
        for i, num in enumerate(nums):
            for index in indexs[num]:
                if (i * index) % k == 0:
                    ans += 1

            indexs[num].append(i)
            
        return ans