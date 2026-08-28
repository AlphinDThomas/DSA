# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        count = 0

        temp = head

        while temp!=None:
            count+=1
            temp =  temp.next
        mid = count//2
        if count == 1:
            return None
        curr = head
        for i in range(count):
            if i+1 == mid:
                curr.next = curr.next.next
            if curr.next is not None:
                curr = curr.next
        return head