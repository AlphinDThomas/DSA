class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans =-1
        for right in range(len(nums)):
            temp1 = sum(nums[0:right])
            temp2 = sum(nums[right+1:len(nums)])
            if temp1 == temp2:
                ans= right
                break
        return ans