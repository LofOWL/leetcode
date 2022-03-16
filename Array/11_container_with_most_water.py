from ast import List

class Solution:
    def maxArea(self, height:List[int]) -> int:
        left = 0
        right = len(height) - 1
        ans = 0
        maxh = max(height)
        while left < right:
            ans = max(ans,(right-left)*min(height[left],height[right]))
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
            if ans >= maxh * (right - left):
                break
        return ans