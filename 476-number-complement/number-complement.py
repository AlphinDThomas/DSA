class Solution:
    def findComplement(self, num: int) -> int:
        
        def tobin(num):
            res = ""
            while num>0:
                digit = num%2
                res = str(digit)+res
                num = num//2
            return res
        
        def complement(num):
            ans = ""
            for i in num:
                if i=="0":
                    ans = ans+"1"
                else:
                    ans = ans+"0"
            return ans
        
        binofnum = tobin(num)
        complementofnum = complement(binofnum)
        return int(complementofnum,2)
