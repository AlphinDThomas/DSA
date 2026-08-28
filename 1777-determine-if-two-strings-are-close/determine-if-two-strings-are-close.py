class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        if len(word1)!=len(word2):
            return False
        word1 = list(word1)
        word2 = list(word2)
        

        dicte1 = dict()
        dicte2 = dict()

        for i in word1:
            if i not in dicte1:
                dicte1[i] = word1.count(i)
        for i in word2:
            if i not in dicte2:
                dicte2[i] = word2.count(i)
        
        if dicte1.keys() != dicte2.keys():
            return False
        
        list1 = []
        list2 = []
        for i in word1:
            list1.append(dicte1[i])
        for j in word2:
            list2.append(dicte2[j])

        if sorted(list1) != sorted(list2):
            return False
        
        return True
        '''

        if len(word1)!=len(word2):
            return False
        dicte1 = dict()
        dicte2 = dict()
        for i in word1:
            if i not in dicte1:
                dicte1[i] = word1.count(i)
        for j in word2:
            if j not in dicte2:
                dicte2[j] = word2.count(j)

        return dicte1.keys() == dicte2.keys() and sorted(dicte1.values()) == sorted(dicte2.values())