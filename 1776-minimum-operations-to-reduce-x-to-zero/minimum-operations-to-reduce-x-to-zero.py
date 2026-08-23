class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        
        target = sum(nums) - x

        maxlen = -1

        left = 0
        currsum =0

        for right in range(len(nums)):

            currsum = currsum + nums[right]

            
            
            while left<=right and currsum>target:
                currsum = currsum - nums[left]
                left+=1
            
            if target == currsum:
                maxlen = max(maxlen, right-left+1)

        if maxlen == -1:
            return -1
        return len(nums) - maxlen