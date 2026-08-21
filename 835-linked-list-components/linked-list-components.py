# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def numComponents(self, head: Optional[ListNode], nums: List[int]) -> int:
        
        nums =  set(nums)

        count = 0
        temp = head

        while temp:
            if temp.val in nums and (temp.next is None or temp.next.val not in nums):
                count+=1
            temp = temp.next
        return count