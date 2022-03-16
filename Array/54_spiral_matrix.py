from ast import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result=[]
        rows =len(matrix)
        if rows<1:
            return result
        colunms = len(matrix[0])
        left = 0
        right = colunms-1
        up = 0 
        down = rows-1
        while True:
            for i in range(left,right+1):
                result.append(matrix[up][i])
            up+=1
            if left>right:
                break
            for i in range(up,down+1):
                result.append(matrix[i][right])
            if up>down:
                break
            right-=1
            for i in range(right,left-1,-1):
                result.append(matrix[down][i])
            if left>right:
                break
            down-=1
            for i in range(down,up-1,-1):
                result.append(matrix[i][left])
            if up>down:
                break
            left+=1
        return result

