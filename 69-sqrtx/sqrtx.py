class Solution:
    def mySqrt(self, x: int) -> int:
        left = 1
        right = x

        while left<=right:

            mid = (left+right)//2

            squared = mid * mid
            if squared == x:
                return mid
            elif squared<x:
                left = mid +1
            elif squared>x:
                right = mid-1
        return right