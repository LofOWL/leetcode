"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        from collections import deque
        s = deque()
        s.appendleft(root)
        if not root:
            return
        cnt = 1
        while len(s):
            t1 = s.pop()
            if t1.left is not None:
                s.appendleft(t1.left)
                s.appendleft(t1.right)
            for _ in range(cnt-1):
                t2 = s.pop()
                t1.next = t2
                t1 = t2
                if t1.left is not None:
                    s.appendleft(t1.left)
                    s.appendleft(t1.right)
                t1.next = None
            cnt *= 2
        return root


class Solution:
    def connect(self, root: 'Node') -> 'Node':
        
        if not root:
            return root
        
        # 从根节点开始
        leftmost = root
        
        while leftmost.left:
            
            # 遍历这一层节点组织成的链表，为下一层的节点更新 next 指针
            head = leftmost
            while head:
                
                # CONNECTION 1
                head.left.next = head.right
                
                # CONNECTION 2
                if head.next:
                    head.right.next = head.next.left
                
                # 指针向后移动
                head = head.next
            
            # 去下一层的最左的节点
            leftmost = leftmost.left
        
        return root 
