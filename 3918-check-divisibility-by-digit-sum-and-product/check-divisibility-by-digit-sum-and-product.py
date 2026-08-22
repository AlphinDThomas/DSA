class Solution:
    def checkDivisibility(self, n: int) -> bool:
        n =  str(n)
        sumn = 0
        productn = 1

        for i in n:
            sumn+=int(i)
            productn = productn*int(i)
        
        total = sumn + productn

        n = int(n)

        return n%total == 0