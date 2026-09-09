class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        num = bin(n)
        if n<=0:
            return False
        list1 = list(num)
        print(list1)
        if list1.count('1') == 1:
            return True
        else:return False