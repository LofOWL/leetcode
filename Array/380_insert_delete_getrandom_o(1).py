from random import choice

class RandomizedSet:

    def __init__(self):
        self.dic = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.dic:
            return False
        # store the index of inserted element
        self.dic[val] = len(self.list)
        self.list.append(val)
        return True 

    def remove(self, val: int) -> bool:
        if val in self.dic:
            last_element, index = self.list[-1], self.dic[val]
            # exchange the order of the element to be deleted and the element at index
            self.list[index] = self.list[-1]
            self.dic[last_element] = index
            self.list.pop()
            del self.dic[val]
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.list)



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()