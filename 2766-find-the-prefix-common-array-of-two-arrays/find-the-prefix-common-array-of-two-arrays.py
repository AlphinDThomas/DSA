class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        
        def check(temp1 , temp2):
            count = 0
            for i in range(len(temp1)):
                if temp1[i] in temp2:
                    count+=1
            return count

        C = []
        for i in range(len(A)):
            temp1 = A[:i+1]
            temp2 = B[:i+1]

            result  = check(temp1,temp2)
            C.append(result)
        return C