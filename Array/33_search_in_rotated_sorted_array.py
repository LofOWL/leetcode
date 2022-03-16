from ast import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        N = len(nums)
        # if N==0:
        #     return -1

        lidx, ridx = 0, N-1
        while lidx<=ridx:
            midx = (lidx + ridx)//2
            # print(lidx, midx, ridx)
            if target==nums[midx]:
                return midx
            elif target==nums[lidx]:
                return lidx
            elif target==nums[ridx]:
                return ridx
            elif nums[lidx]<nums[midx]:
                if nums[lidx] <= target < nums[midx]:
                    ridx = midx - 1
                else:
                    lidx = midx + 1
            else:
                if nums[midx] < target <= nums[ridx]:
                    lidx = midx + 1
                else:
                    ridx = midx - 1
        return -1


    def search_recur(self, nums: List[int], target: int) -> int:
        N = len(nums)
        if N==0:
            return -1
        
        idx = N//2
        if target==nums[idx]:
            return idx
        elif target<nums[idx]:
            return idx + self.search(nums[idx:])
        else:
            return self.search(nums[:idx])