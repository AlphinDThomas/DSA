class Solution:
    def minChanges(self, n: int, k: int) -> int:
        binaryn=""

        while n>0:
            remainder = n%2
            binaryn+= str(remainder)
            n = n//2
        binaryn = binaryn[::-1]
        

        binaryk = ""
        while k>0:
            remainder = k%2
            binaryk += str(remainder)
            k = k//2
        binaryk = binaryk[::-1]
        
        if len(binaryn)>len(binaryk):
            binaryk = "0"*(len(binaryn)-len(binaryk)) + binaryk
        elif len(binaryk)>len(binaryn):
            binaryn = "0"*(len(binaryk)-len(binaryn)) + binaryn
        
        print(binaryn)
        print(binaryk)

        count = 0
        for i in range(len(binaryn)):
            if binaryn[i]=="1" and binaryk[i]=="0":
                count+=1
            elif binaryn[i]=="0" and binaryk[i]=="1":
                return -1
        return count