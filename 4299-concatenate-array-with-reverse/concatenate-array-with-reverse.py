class Solution:
    def concatWithReverse(self, nums: list[int]) -> list[int]:
        newarr = nums[::-1]

        return nums+newarr