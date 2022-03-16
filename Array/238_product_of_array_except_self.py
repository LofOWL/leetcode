from ast import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        tmp_first = [1]
        tmp_second = [1]
        tmp = 1
        for num in nums[:-1]:
            tmp *= num
            tmp_first.append(tmp)
        tmp = 1
        for num in nums[::-1][:-1]:
            tmp *= num
            tmp_second.append(tmp)
        result = [first * second for first, second in zip(tmp_first, tmp_second[::-1])]
        return result