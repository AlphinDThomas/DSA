class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        len1 = len(word1)
        len2 = len(word2)
        i = 0
        j = 0
        substring = ""
        while i<len1 and j<len2:
            substring += word1[i]
            substring += word2[j]
            i+=1
            j+=1
        
        if i<len1:
            while i<len1:
                substring += word1[i]
                i+=1
        if j<len2:
            while j<len2:
                substring += word2[j]
                j+=1
        return substring