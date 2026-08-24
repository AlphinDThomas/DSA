# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        nodes= []
        temp = head
        while temp!= None:
            nodes.append(temp.val)
            temp = temp.next
        print(nodes)
        res = []
        for i in range(0, len(nodes),k):
            temp = nodes[i:i+k]
            if len(temp)==k:
                temp = temp[::-1]
            res = res + temp
        print(res)
        
        dummy = ListNode(res[0])
        newhead = dummy
        for i in range(1,len(res)):
            newnode = ListNode(res[i])
            dummy.next = newnode
            dummy =  dummy.next
        return newhead
            