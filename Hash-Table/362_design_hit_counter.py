class HitCounter:

    def __init__(self):
        self.count_hash = dict()


    def hit(self, timestamp: int) -> None:
        self.count_hash[timestamp] = self.count_hash.get(timestamp,0) + 1


    def getHits(self, timestamp: int) -> int:
        res = 0
        k = list(self.count_hash.keys())
        for key in k:
            if timestamp - key < 300:
                res = res + self.count_hash[key]
        return res



# Your HitCounter object will be instantiated and called as such:
# obj = HitCounter()
# obj.hit(timestamp)
# param_2 = obj.getHits(timestamp)