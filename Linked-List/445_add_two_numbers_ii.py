# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # use stacks to save node values 
        stk1 = []
        stk2 = []
        p1 = l1 
        p2 = l2 
        while p1!=None:
            stk1.append(p1.val)
            p1 = p1.next 
        while p2!=None:
            stk2.append(p2.val)
            p2 = p2.next 
        res = []
        carry = 0 
        while stk1 or stk2 or carry>0:
            val = carry 
            if stk1:
                val += stk1.pop()
            if stk2:
                val += stk2.pop()
            res.append(val%10)
            # update the carry 
            carry = val//10 
        # print(res)
        # generate the result list 
        dummy = ListNode(-99999)
        p = dummy 
        while res:
            p.next = ListNode(res.pop())
            p = p.next 
        return dummy.next 

