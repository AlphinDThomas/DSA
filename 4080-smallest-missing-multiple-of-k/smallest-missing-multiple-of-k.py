class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        i = 1
        val = k
        while True:
            if val not in nums:
                return val
            i+=1
            val = k * i
            