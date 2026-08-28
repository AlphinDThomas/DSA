class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        left = 0
        currsum = 0
        maxsum = float('-inf')
        for right in range(len(nums)):

            currsum += nums[right]

            while right-left+1 > k:
                currsum = currsum - nums[left]
                left+=1
            
            if right-left+1 == k:
                maxsum = max(maxsum,currsum)
            
        return maxsum/k