class Solution:
    def commonChars(self, words: list[str]) -> list[str]:
        alpha = "abcdefghijklmnopqrstuvwxyz"
        res = []
        for i in alpha:
            min_count = 100
            for word in words:
                count = word.count(i)
                min_count = min(min_count,count)
            for j in range(min_count):
                res.append(i)
        return res