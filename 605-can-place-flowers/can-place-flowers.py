class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        print(flowerbed)
        nums = flowerbed.copy()
        for i in range(1,len(nums)-1):
            if nums[i]==0 and nums[i-1]==0 and nums[i+1]==0:
                nums[i] = 1
                n-=1
        if n<=0:
            return True
        else:
            return False

        
