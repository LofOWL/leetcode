from ast import List
import collections

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        输入：tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"], n = 2, 输出：16, 解释：一种可能的解决方案是：
        A -> B -> C -> A -> D -> E -> A -> F -> G -> A -> (待命) -> (待命) -> A -> (待命) -> (待命) -> A
        公式题
        时空：都为O(n)
        """
        counter=collections.Counter(tasks) # keys()：Task, values(): Task_num
        m=0   #最大任务数量
        c=0   #最大任务数量的个数
        for val in counter.values(): # 找到m,c即可根据公式求解
            if val > m:
                m = val
                c = 1
            elif val == m:
                c += 1
        return max(len(tasks),(n+1)*(m-1)+c) # len(tasks)是一个下界