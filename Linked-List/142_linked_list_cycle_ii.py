# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        dic={}
        p=head
        index=0
        while p:
            if p not in dic:
                dic[p]=index
                index+=1
                p=p.next
            else:
                return p
        return None