class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        res = []
        for i in nums:
            if i>=k:
                res.append(i)
        return len(nums)-len(res)