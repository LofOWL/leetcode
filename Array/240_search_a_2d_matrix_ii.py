from ast import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        i, j = m - 1, 0
        while i >= 0 and j < n:
            # 从左下角开始，
            # 小于目标值，左边的列可以放弃，向右移动
            #大于目标值， 下面的行可以放弃，向上移动
            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                j += 1
            else:
                i -= 1
        return False
        