class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        left = 0
        zerocount = 0
        longest = 0
        for right in range(len(nums)):

            if nums[right]==0:
                zerocount+=1
            
            while zerocount>1:
                if nums[left]==0:
                    zerocount-=1
                left+=1
            if zerocount<=1:
                longest = max(longest,right-left)

        return longest