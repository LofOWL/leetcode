from ast import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        start = step = 0
        end = 1
        while end < len(nums):
            max_num = 0
            for i in range(start ,end):
                max_num=max(max_num,i+nums[i])
            start, end = end, max_num+1
            step += 1
        return step