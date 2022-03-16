from ast import List
import collections

class Solution:
    def connectSticks(self, sticks: List[int]) -> int:

        #haffman树

        # 实现1，直接heap实现

        # heap=sticks[:]

        # heapq.heapify(heap)
        # ans=0
        # while len(heap)>1:
        #     v=heapq.heappop(heap)+heapq.heappop(heap)
        #     ans+=v
        #     heapq.heappush(heap,v)
        # return ans

        # 用两个有序列表实现，其中一个是单向提取(可以是stack)，另一个则是插入和提取同时操作

        stack=sticks[:]
        stack.sort(reverse=True)
        queue=collections.deque()
        ans=0
        while len(stack)+len(queue)>1:
            if not queue:
                val=stack.pop()+stack.pop()
            elif not stack:
                val=queue.popleft()+queue.popleft()
            else:
                val=0
                for k in range(2):
                    if stack and (not queue or stack[-1]<queue[0]):
                        val+=stack.pop()
                    else:
                        val+=queue.popleft()
            ans+=val
            queue.append(val)

        return ans