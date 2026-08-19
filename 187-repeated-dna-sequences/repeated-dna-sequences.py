class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seen = set()
        res = set()
        for i in range(len(s)-9):
            temp = s[i:i+10]
            if temp in seen:
                res.add(temp)
            seen.add(temp)
        return list(res)