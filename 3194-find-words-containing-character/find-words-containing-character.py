class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        ans = []
        count = 0
        for i in range(len(words)):
            if x in words[i]:
                ans.append(i)
            

        return ans