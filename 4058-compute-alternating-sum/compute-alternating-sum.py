class Solution:
    def alternatingSum(self, nums: List[int]) -> int:
        evensum = 0

        for i in range(0,len(nums),2):
            evensum += nums[i]

        oddsum = 0
        for i in range(1,len(nums),2):
            oddsum += nums[i]
        return evensum-oddsum