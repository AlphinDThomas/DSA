class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        
        list1 = list(s)
        list1 = list(set(list1))
        flag = 0
        newcount = 0
        for i in range(len(s)):
            for j in range(i+1,len(s)+1):
                temp = s[i:j]
                for ch in temp:
                    if temp.count(ch)>2:
                        flag=1
                if flag == 0:
                    newcount= max(newcount , len(temp))
                flag = 0
        return newcount