from ast import List

class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n =len(nums)
        min_idx = -1
        for i in reversed(range(n-1)):
            temp_min = float('inf')
            min_idx = -1
            for j in range(i+1, n):
                if nums[j] > nums[i] and nums[j]<=temp_min:
                    temp_min = nums[j]
                    min_idx = j
            if min_idx != -1:
                nums[min_idx], nums[i] = nums[i],nums[min_idx]
                left, right = i+1, n-1
                while left < right:
                    nums[left],nums[right] = nums[right],nums[left]
                    left += 1
                    right -= 1
                break
        if min_idx == -1:
            #print(nums)
            left, right = 0, n-1
            while left < right:
                #print('left:', left,'right:',right)
                nums[left],nums[right] = nums[right],nums[left]
                left += 1
                right -= 1 
            
            
            


