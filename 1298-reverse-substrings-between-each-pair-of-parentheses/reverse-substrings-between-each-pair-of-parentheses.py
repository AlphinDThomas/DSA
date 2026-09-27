class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = []
        for i in s:
            if i == ")":
                temp = []
                while stack[-1]!="(":
                    temp.append(stack.pop())
                stack.pop()
                for j in temp:
                    stack.append(j)
            else:
                stack.append(i)
        return ''.join(stack)
