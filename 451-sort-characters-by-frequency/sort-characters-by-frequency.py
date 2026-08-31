class Solution:
    def frequencySort(self, s: str) -> str:
        

        dicte = dict()
        for ch in s:
            if ch in dicte:
                dicte[ch]+=1
            else:
                dicte[ch]=1

        sorteddicte = sorted(dicte,key=dicte.get,reverse=True)

        result = ""

        for i in sorteddicte:
            result = result + i*dicte[i]
        return result