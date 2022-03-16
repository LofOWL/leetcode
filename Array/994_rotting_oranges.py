from ast import List
import collections
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        count, queue = 0, collections.deque()
        m, n = len(grid), len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i,j,0))
                elif grid[i][j] == 1:
                    count += 1
        if not count: return 0
        while queue:
            i, j, step = queue.popleft()
            for di, dj in [(1,0), (-1,0), (0,1), (0,-1)]:
                ni, nj = i+di, j+dj
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    count -= 1
                    grid[ni][nj] = 2
                    if not count: return step+1
                    queue.append((ni,nj,step+1))
        return -1