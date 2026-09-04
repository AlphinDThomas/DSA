class Solution:
    def firstStableIndex(self, nums: list[int], k: int) -> int:
        
        for i in range(len(nums)):
            leftmax = max(nums[:i+1])
            rightmin = min(nums[i:])
            
            score = leftmax - rightmin

            if score<=k:
                return i
        return -1
