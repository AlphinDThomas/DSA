class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        
        seenbyme = set()
        spcl = set()

        for i in range(len(nums)):
            if nums[i] not in seenbyme:
                seenbyme.add(nums[i])
                spcl.add(nums[i])
            elif nums[i]!=nums[i-1]:
                if nums[i] in seenbyme:
                    spcl.discard(nums[i])
        return len(spcl)