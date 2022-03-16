from ast import List

class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        n = n % 14
        if not n:
            n = 14
        for _ in range(n):
            cells = [0] + [cells[i-1]^cells[i+1]^1 for i in range(1,7)] + [0]
        return cells
        