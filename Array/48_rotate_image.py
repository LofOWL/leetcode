from ast import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n-1):
            for j in range(i, n-i-1):
                tmp = matrix[i][j]
                for _ in range(4):
                    tmp_in = matrix[j][n-i-1]
                    matrix[j][n-i-1] = tmp
                    tmp = tmp_in
                    i, j = j, n-i-1
        
