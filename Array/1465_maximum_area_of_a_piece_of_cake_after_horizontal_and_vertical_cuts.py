from ast import List

class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        mod = pow(10,9) + 7
        horizontalCuts = sorted(horizontalCuts)
        verticalCuts = sorted(verticalCuts)
        maxHigh = horizontalCuts[0] - 0
        maxWide = verticalCuts[0] - 0
        maxHigh = (h - horizontalCuts[-1]) if (h - horizontalCuts[-1]) > maxHigh else maxHigh
        maxWide = (w - verticalCuts[-1]) if (w - verticalCuts[-1]) > maxWide else maxWide
        for i in range(len(horizontalCuts)-1):
            maxHigh = (horizontalCuts[i+1] - horizontalCuts[i]) if (horizontalCuts[i+1] - horizontalCuts[i]) > maxHigh else maxHigh  
        for i in range(len(verticalCuts)-1):
            maxWide = (verticalCuts[i+1]-verticalCuts[i]) if (verticalCuts[i+1] - verticalCuts[i]) > maxWide else maxWide
        return (maxHigh * maxWide) % mod