# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        temp = head.next
        res = []
        sum = 0
        while temp!=None:
            if temp.val!=0:
                sum = sum + temp.val
                temp =  temp.next
                
            elif temp.val == 0:
                res.append(sum)
                sum = 0
                temp =  temp.next
        print(res)

        newhead =  ListNode(res[0])
        curr = newhead
        for i in res[1:]:
            curr.next = ListNode(i)
            curr = curr.next
        return newhead