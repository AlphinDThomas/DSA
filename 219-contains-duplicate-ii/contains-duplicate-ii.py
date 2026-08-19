class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        dicte = dict()

        for i in range(len(nums)):

            if nums[i] in dicte:
                if i - dicte[nums[i]]<=k:
                    return True
            dicte[nums[i]] = i
        return False