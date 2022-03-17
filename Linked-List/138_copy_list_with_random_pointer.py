class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        dic = {}
        if head:
            new_head = Node(head.val)
            dic[head] = new_head
        else:
            return None
        
        prev_new_node = new_head
        curr_old_node = head.next
        while curr_old_node:
            new_node = Node(curr_old_node.val)
            dic[curr_old_node] = new_node
            prev_new_node.next = new_node
            prev_new_node = new_node
            curr_old_node = curr_old_node.next
        
        curr_old_node = head
        curr_new_node = new_head
        while curr_old_node:
            curr_new_node.random = dic.get(curr_old_node.random)
            curr_old_node = curr_old_node.next
            curr_new_node = curr_new_node.next
        
        return new_head