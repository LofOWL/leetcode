from ast import List
import collections

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = collections.Counter(nums)
        # heap = []
        # for key, value in counter.items():
        #     if len(heap) >= k:
        #         if value > heap[0][0]:
        #             heapq.heapreplace(heap, (value, key))
        #     else:
        #         heapq.heappush(heap, (value, key))
        # return [num[1] for num in heap]
        ans = sorted(counter, key=lambda num:(-counter[num]))
        return ans[: k]