from ast import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        dp=1<<amount
        res=0
        while dp:
            tmp=0
            res+=1
            for i in coins:
                tmp|=dp>>i
            if tmp&1:
                return res
            dp=tmp
        return -1