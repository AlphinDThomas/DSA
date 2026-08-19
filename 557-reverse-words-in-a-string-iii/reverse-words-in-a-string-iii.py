class Solution:
    def reverseWords(self, s: str) -> str:
        list1 = s.split()
        res = []
        for i in list1:
            substring = ""
            for j in range(len(i)-1,-1,-1):
                substring = substring + i[j]
            res.append(substring)
        
        news= ""
        print(res)
        newsub = ""
        for i in res:
            newsub = newsub + i + " "
        return newsub[0:len(newsub)-1]