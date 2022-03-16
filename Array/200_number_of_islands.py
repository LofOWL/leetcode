from ast import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            #将当前访问节点置空
            grid[row][col] = '0'

            #依次访问其上下左右的节点 
            if row != 0 and grid[row-1][col] == '1':
                dfs(row -1, col)
            if row != n_r - 1 and grid[row+1][col] == '1':
                dfs(row + 1, col)
            if col != 0 and grid[row][col-1] == '1':
                dfs(row, col- 1)
            if col != n_c - 1 and grid[row][col+1] == '1':
                dfs(row, col + 1)
        
        n_r = len(grid)
        n_c = len(grid[0])
        ans = 0
        for row in range(0, n_r):
            for col in range(0, n_c):
                if grid[row][col] == '1':
                    ans += 1
                    dfs(row,col)
                