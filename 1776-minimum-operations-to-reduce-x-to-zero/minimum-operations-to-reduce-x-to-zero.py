class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        target = sum(nums) - x
        currsum = 0
        maxtargetlen = -1
        left = 0
        for right in range(len(nums)):

            currsum = currsum + nums[right]

            
            while left<=right and currsum>target:
                currsum = currsum - nums[left]
                left = left + 1

            if currsum == target:
                maxtargetlen = max(maxtargetlen,(right-left+1))
        if maxtargetlen==-1:
            return -1
        return len(nums)-maxtargetlen