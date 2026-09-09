class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        
        freq = dict()

        for num in nums:
            if num not in freq:
                freq[num]=1
            else:
                freq[num]+=1
            
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if freq[nums[i]]>freq[nums[j]]:
                    nums[i],nums[j] = nums[j],nums[i]

                elif freq[nums[i]] ==  freq[nums[j]]:
                    if nums[i]<nums[j]:
                        nums[i],nums[j] = nums[j],nums[i]
        return nums