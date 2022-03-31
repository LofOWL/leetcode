from ast import List
import collections

class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(A)
        n = len(B[0])
        posA = self.getSparseRepresentation(A)
        posB = self.getSparseRepresentation(B)
        res = [[0 for i in range(n)] for j in range(m)]
        for valA, xA, yA in posA:
            for valB, xB, yB in posB:
                if yA == xB and valA != 0 and valB != 0:
                    res[xA][yB] += valA * valB
        return res
    
    def getSparseRepresentation(self, A):
        posList = []
        m = len(A)
        n = len(A[0])
        for i in range(m):
            for j in range(n):
                if A[i][j] != 0:
                    posList.append([A[i][j],i,j])
        return posList

class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        r1 = len(mat1)
        r2 = len(mat2)

        if r1 == 0 or r2 == 0:
            return []
        
        c1 = len(mat1[0])
        c2 = len(mat2[0])

        res = [[0] * c2 for _ in range(r1)]
        mat1_ = collections.defaultdict(dict)
        for r in range(r1):
            for c in range(c1):
                if mat1[r][c] != 0:
                    mat1_[r][c] = mat1[r][c]
        
        mat2_ = collections.defaultdict(dict)
        for c in range(c2):
            for r in range(r2):
                if mat2[r][c] != 0:
                    mat2_[c][r] = mat2[r][c]

        
        for k1, v1 in mat1_.items():
            for k2, v2 in mat2_.items():
                res[k1][k2] = sum([v * v2.get(k, 0) for k, v in v1.items()])
        
        return res

