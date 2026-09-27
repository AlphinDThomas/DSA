class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seenmap = dict()
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in seenmap:
                return [seenmap[complement],i]
            seenmap[nums[i]] = i
        return []