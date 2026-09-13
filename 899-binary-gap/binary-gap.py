class Solution:
    def binaryGap(self, n: int) -> int:
        
        def tobin(n):
            res = ""
            while n>0:
                digit = n%2
                n = n//2
                res = str(digit) + res 
            return res
        res = tobin(n)
        list1 = list(res)
        if list1.count('1')<=1:
            return 0
        firstgap = -1
        secgap = -1
        maxgap = -1
        for i in range(len(list1)):
            if list1[i]=='1' and firstgap==-1:
                firstgap = i
            elif list1[i]=='1' and secgap==-1:
                secgap = i
                maxgap = max(maxgap,(secgap-firstgap))
                firstgap = secgap
                secgap = -1
        return maxgap