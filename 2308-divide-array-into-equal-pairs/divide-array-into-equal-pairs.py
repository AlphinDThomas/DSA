class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        
        newset = set(nums)
        for i in newset:
            if nums.count(i)%2 != 0:
                return False
        return True