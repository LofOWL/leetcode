# Definition for a binary tree node.
from ast import List
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        from collections import defaultdict, deque
        if not root: return []
        q = deque()
        q.appendleft((0,root))
        d = defaultdict(list)
        while q:   
            index,node = q.pop()
            d[index].append(node.val)
            if node.left:
                q.appendleft((index-1,node.left))
            if node.right:
                q.appendleft((index+1,node.right))
        sort_d = sorted(d.items(), key = lambda x: x[0])
        return [l[1] for l in sort_d]
        



