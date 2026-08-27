class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        
        first = 999999999999
        second= 999999999999

        for i in nums:
            if i<=first:
                first = i
            elif i<=second:
                second = i
            else:
                return True
        return False