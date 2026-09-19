class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        left = 1 
        right = max(piles)
        res = max(piles)
        
        while left<=right:
            mid = (left+right)//2
            hours = 0
            for p in piles:
                hours = hours + math.ceil(p/mid)
            
            if hours>h:
                left = mid + 1
            elif hours<=h:
                right = mid - 1
                res = min(res,mid)
        return res