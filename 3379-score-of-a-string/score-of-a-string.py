class Solution:
    def scoreOfString(self, s: str) -> int:
        res = []

        for i in s:
            res.append(ord(i))
        
        result = []

        for i in range(1,len(res)):
            temp = abs(res[i]-res[i-1])
            result.append(temp)
        return sum(result)
