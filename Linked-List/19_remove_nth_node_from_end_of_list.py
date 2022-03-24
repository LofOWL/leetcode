# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        A=[head]
        while(A[-1].next):
            A.append(A[-1].next)
        if(len(A)>n):
            A[len(A)-n-1].next= A[len(A)-n-1].next.next
            A[len(A)-n]=None
        else:
            head=head.next
        return head