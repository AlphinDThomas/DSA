class Solution:
    def kthLargestNumber(self, nums: List[str], k: int) -> str:
        
        list1 = []
        for i in nums:
            list1.append(int(i))

        def bubblesort(nums):
            for i in range(len(nums)):
                for j in range(len(nums)-i-1):
                    if nums[j]>nums[j+1]:
                        nums[j],nums[j+1] = nums[j+1],nums[j]
            return nums
        
        list1.sort()
        return str(list1[-k])