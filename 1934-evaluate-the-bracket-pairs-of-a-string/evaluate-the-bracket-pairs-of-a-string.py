class Solution:
    def evaluate(self, s: str, knowledge: list[list[str]]) -> str:
        knowledgebase = dict()

        for i in knowledge:
            knowledgebase[i[0]] = i[1]

        print(knowledgebase)
        list1 = []
        res = ""
        substring = ""
        flag = 0
        for i in range(len(s)):
            if s[i] == "(":
                flag = 1
            elif s[i]==")":
                flag = 0
                if substring in knowledgebase:
                    temp = knowledgebase[substring]
                    res = res + temp
                    substring = ""
                else:
                    res = res + "?"
                    substring = ""
            elif flag == 1:
                substring+= s[i]
            elif flag==0:
                res = res + s[i]
        return res
            