# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        ans = []
        curr = head

        def gcd(x,y):
            if x == 0:
                return y
            return gcd(y%x,x)

        if head and not head.next:
            return head
        while curr.next!=None:
            
            ans =  gcd(curr.val , curr.next.val)
            newnode = ListNode(ans)
            temp = curr.next
            curr.next = newnode
            newnode.next = temp
            curr = newnode.next
        
        return head