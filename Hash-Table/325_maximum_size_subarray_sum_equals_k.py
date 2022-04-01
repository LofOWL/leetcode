from ast import List

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        pre_sum = 0
        sum_to_index = {}
        sum_to_index[0] = -1
        res = 0
        for i in range(len(nums)):
            pre_sum += nums[i]
            
            #print(pre_sum )
            if pre_sum - k in sum_to_index:
                #print(pre_sum, pre_sum -k, sum_to_index[pre_sum-k])
                res = max(res, i - sum_to_index[pre_sum - k])
            if pre_sum not in sum_to_index:
                sum_to_index[pre_sum] = i
        
        #print(sum_to_index)
        
        return res
