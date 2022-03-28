class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        sum = 0
        dic = dict()
        dic[0] = 1
        for i in range(len(nums)):
            sum += nums[i]
            
            if(sum - k in dic):
                ans+=dic[sum-k]
            
            if(sum in dic):
                dic[sum] +=1
            else:
                dic[sum] = 1
        return ans
