class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        
        minval = 1000000000

        for i in range(len(nums)):
            if len(str(nums[i]))==1 and i == nums[i]:
                minval = min(nums[i],minval)
            elif len(str(nums[i]))>1:
                tempsum = 0 
                for j in str(nums[i]):
                    tempsum+=int(j)
                if tempsum == i:
                    minval = min(minval,tempsum)
        if minval == 1000000000:
            return -1
        return minval
