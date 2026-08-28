class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        prefixarr = [0]
        prev = 0
        for i in gain:
            prev =  prev + i
            prefixarr.append(prev)
        return max(prefixarr)