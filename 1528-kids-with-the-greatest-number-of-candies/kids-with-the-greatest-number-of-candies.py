class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        def checker(num,extraCandies):

            flag = 0
            for i in candies:
                if num+extraCandies<i:
                    flag = 1
                elif num+extraCandies==i:
                    continue
            if flag==0:
                return True
            else:
                return False
        
        res = []
        for j in candies:
            result = checker(j,extraCandies)
            res.append(result)
        return res