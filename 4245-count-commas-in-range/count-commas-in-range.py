class Solution:
    def countCommas(self, n: int) -> int:
        
        if n<1000:
            return 0
        if n>=1000 and n<=9999:
            return n-1000+1
        if n>9999 and n<100000:
            return n-10000 + 1 + 9000
        if n==100000:
            return 2 + 9000+ 89999
            