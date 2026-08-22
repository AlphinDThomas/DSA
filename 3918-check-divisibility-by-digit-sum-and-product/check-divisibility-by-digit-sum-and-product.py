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

        if n%total == 0:
            return True
        return False