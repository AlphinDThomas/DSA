class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        ans =-1
        total = sum(nums)
        leftsum = 0
        for i in range(len(nums)):
            
            
            rightsum = total - leftsum - nums[i]

            if leftsum == rightsum:
                return i
            leftsum = leftsum + nums[i]
        return -1
