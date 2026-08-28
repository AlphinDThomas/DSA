# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        res = []
        temp = head
        while temp!=None:
            res.append(temp.val)
            temp = temp.next
        maxsum = -1
        left = 0
        print(res)
        right = len(res)-1
        print(left)
        print(right)
        while left<right:
            maxsum = max(maxsum, res[left]+res[right])
            left+=1
            right-=1
        return maxsum