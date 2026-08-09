class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = []
        substr = ""
        for i in s:
            if i in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890":
                substr+=i
            else:
                if substr!="":
                    list1.append(substr)
                substr = ""
        if substr!="":
            list1.append(substr)
        print(list1)

        substring = ""
        for i in range(len(list1)-1,-1,-1):
            substring += list1[i] + " "
        
        return substring[0:len(substring)-1]