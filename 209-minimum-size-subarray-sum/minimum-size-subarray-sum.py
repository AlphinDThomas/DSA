class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:


        left = 0
        minlen = 9999999
        currsum = 0
        for right in range(len(nums)):

            currsum = currsum + nums[right]

            while currsum>=target:  
                currsum = currsum - nums[left]
                minlen = min(minlen , right-left+1)
                left+=1
                
        if minlen == 9999999:
            return 0
        return minlen