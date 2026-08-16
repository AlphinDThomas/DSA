class Solution:
    def digitFrequencyScore(self, n: int) -> int:
        sum = 0
        for i in str(n):
            sum+=int(i)
        return sum
