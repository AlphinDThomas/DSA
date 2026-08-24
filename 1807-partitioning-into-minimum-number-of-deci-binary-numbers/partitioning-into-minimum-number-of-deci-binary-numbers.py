class Solution:
    def minPartitions(self, n: str) -> int:
        
        maxele = -1
        for i in n:
            maxele = max(maxele,int(i))
        return maxele