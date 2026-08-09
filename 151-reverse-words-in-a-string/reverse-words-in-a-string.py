class Solution:
    def reverseWords(self, s: str) -> str:
        
        list1 = s.split()
        list2 = list1[::-1]
        substr = ""
        for i in list2:
            substr+= i + " "
        return substr[0:len(substr)-1]