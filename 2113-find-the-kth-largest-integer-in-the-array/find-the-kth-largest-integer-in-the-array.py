class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        for i in range(len(nums)):
            nums[i] = int(nums[i]) * -1
        
        heapq.heapify(nums)

        for _ in range(k-1):
            heapq.heappop(nums)
        return str(-heapq.heappop(nums))