class Solution:
    def validStrings(self, n: int) -> List[str]:
        if n == 1:
            return ["0","1"]
        target = n
        def binarygen(n):
            binary= ""
            while n>0:
                digit = n%2
                binary = str(digit) + binary
                n = n//2
            return binary

        res = []
        i=0
        while True:
            bi = binarygen(i).zfill(target)
            bi = str(bi)
            if len(bi) == target:
                flag = 0
                for j in range(len(bi)-1):
                    if bi[j] == "0" and bi[j+1]== "0":
                        flag = 1
                if flag == 0:
                    res.append(bi)
                i+=1
            elif len(bi)>target:
                break
            else:
                i+=1
        print(res)
        return res