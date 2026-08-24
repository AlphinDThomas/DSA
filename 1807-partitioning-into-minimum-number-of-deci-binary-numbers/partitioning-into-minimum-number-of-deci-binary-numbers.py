class Solution:
    def minPartitions(self, n: str) -> int:
        
        res = []
        for i in n:
            res.append(int(i))
        return max(res)