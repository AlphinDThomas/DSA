class Solution:
    def isBalanced(self, num: str) -> bool:
        
        odd = []
        even = []

        for i in range(1,len(num),2):
            odd.append(int(num[i]))
        for j in range(0,len(num),2):
            even.append(int(num[j]))

        return sum(odd) == sum(even)